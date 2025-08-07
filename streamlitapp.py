import streamlit as st
import streamlit.components.v1 as components
import os
from dotenv import load_dotenv
import time
from RoboGPT import RoboGPT
from datetime import datetime

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="RoboGPT - AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for futuristic styling
with open("UI.css", "r") as f:
    css_content = f.read()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables for multi-chat"""
    if "robogpt" not in st.session_state:
        st.session_state.robogpt = RoboGPT()
    if "chats" not in st.session_state:
        st.session_state.chats = {}
    if "current_chat_id" not in st.session_state or st.session_state.current_chat_id not in st.session_state.chats:
        chat_id = datetime.now().strftime("%Y%m%d%H%M%S")
        st.session_state.chats[chat_id] = {"name": "New Chat", "messages": []}
        st.session_state.current_chat_id = chat_id
    if "is_generating" not in st.session_state:
        st.session_state.is_generating = False
    if "rename_mode" not in st.session_state:
        st.session_state.rename_mode = None
    if "rename_value" not in st.session_state:
        st.session_state.rename_value = ""

def create_floating_particles():
    particles_html = """
    <div id="particles-container" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: -1;"></div>
    <script>
    function createParticles() {
        const container = document.getElementById('particles-container');
        if (container && container.children.length === 0) {
            for (let i = 0; i < 20; i++) {
                const particle = document.createElement('div');
                particle.style.cssText = `
                    position: absolute;
                    width: 2px;
                    height: 2px;
                    background: #00ffff;
                    border-radius: 50%;
                    box-shadow: 0 0 6px #00ffff;
                    left: ${Math.random() * 100}%;
                    animation: float ${10 + Math.random() * 10}s infinite linear;
                    animation-delay: ${Math.random() * 15}s;
                `;
                container.appendChild(particle);
            }
        }
    }
    const style = document.createElement('style');
    style.textContent = `@keyframes float { 0% { transform: translateY(100vh) translateX(0px); opacity: 0; } 10% { opacity: 1; } 90% { opacity: 1; } 100% { transform: translateY(-100px) translateX(100px); opacity: 0; } }`;
    document.head.appendChild(style);
    createParticles();
    </script>
    """
    components.html(particles_html, height=0)

def main():
    initialize_session_state()
    create_floating_particles()

    # --- SIDEBAR: Chat Session Management ---
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1.2rem 0;">
            <h2>🤖 RoboGPT</h2>
            <p>Neural Interface v2.0</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='sidebar-chat-header'>💬 <b>Chats</b></div>", unsafe_allow_html=True)
        
        for chat_id, chat in st.session_state.chats.items():
            is_active = chat_id == st.session_state.current_chat_id
            with st.container():
                if st.session_state.rename_mode == chat_id:
                    # Rename mode: show input and save/cancel buttons horizontally
                    cols = st.columns([6,1,1])
                    with cols[0]:
                        st.session_state.rename_value = st.text_input(
                            "Rename chat", 
                            value=st.session_state.rename_value or chat['name'], 
                            key=f"rename_input_{chat_id}", 
                            label_visibility="collapsed"
                        )
                    with cols[1]:
                        if st.button("💾", key=f"save_rename_{chat_id}", help="Save chat name", use_container_width=True):
                            new_name = st.session_state.rename_value.strip()
                            if new_name:
                                st.session_state.chats[chat_id]['name'] = new_name
                            st.session_state.rename_mode = None
                            st.session_state.rename_value = ""
                            st.rerun()
                    with cols[2]:
                        if st.button("❌", key=f"cancel_rename_{chat_id}", help="Cancel rename", use_container_width=True):
                            st.session_state.rename_mode = None
                            st.session_state.rename_value = ""
                            st.rerun()
                else:
                    cols = st.columns([8,1,1])
                    with cols[0]:
                        if st.button(f"{chat['name']}", key=f"select_{chat_id}", help="Switch to this chat", use_container_width=True):
                            st.session_state.current_chat_id = chat_id
                            st.rerun()
                    with cols[1]:
                        if st.button("📝", key=f"rename_{chat_id}", help="Rename chat", use_container_width=True):
                            st.session_state.rename_mode = chat_id
                            st.session_state.rename_value = chat['name']
                            st.rerun()
                    with cols[2]:
                        if st.button("🗑️", key=f"delete_{chat_id}", help="Delete chat", use_container_width=True):
                            del st.session_state.chats[chat_id]
                            if st.session_state.chats:
                                st.session_state.current_chat_id = next(iter(st.session_state.chats))
                            else:
                                new_id = datetime.now().strftime("%Y%m%d%H%M%S")
                                st.session_state.chats[new_id] = {"name": "New Chat", "messages": []}
                                st.session_state.current_chat_id = new_id
                            st.session_state.rename_mode = None
                            st.session_state.rename_value = ""
                            st.rerun()
                            
        if st.button("➕ New Chat", key="new_chat", use_container_width=True):
            new_id = datetime.now().strftime("%Y%m%d%H%M%S")
            st.session_state.chats[new_id] = {"name": f"Chat {len(st.session_state.chats)+1}", "messages": []}
            st.session_state.current_chat_id = new_id
            st.session_state.rename_mode = None
            st.session_state.rename_value = ""
            st.rerun()
            
        st.markdown("---")
        
        with st.expander("📊 System Status", expanded=True):
            try:
                test_response = st.session_state.robogpt.generate("Hello")
                st.markdown('<div class="status-indicator"><div class="status-dot"></div><span>Neural Core Online</span></div>', unsafe_allow_html=True)
            except Exception as e:
                st.markdown('<div class="status-indicator"><div class="status-dot" style="background: var(--danger); box-shadow: 0 0 10px var(--danger);"></div><span>Neural Core Offline</span></div>', unsafe_allow_html=True)

    # --- MAIN CONTENT AREA ---
    main_container = st.container()
    
    with main_container:
        # --- MAIN HEADER - Compact ---
        st.markdown("""
        <div class="main-header">
            <h1>🤖 RoboGPT</h1>
            <p>Advanced Robotics Engineering Assistant</p>
            <p>Neural network powered robotics consultation system</p>
        </div>
        """, unsafe_allow_html=True)

        # --- CAPABILITIES SECTION - Compact ---
        st.markdown("""
        <div class="capabilities-section">
            <div class="capabilities-title">
                <span>RoboGPT Capabilities</span>
            </div>
            <div class="capabilities-bar">
                <div style="display: flex; gap: 1rem; justify-content: center; align-items: stretch; flex-wrap: wrap;">
                    <div class="feature-card">
                        <strong>🔧 Code Analysis</strong>
                        <small>C/C++, Python, ROS debugging</small>
                    </div>
                    <div class="feature-card">
                        <strong>🧭 Navigation AI</strong>
                        <small>SLAM, path planning systems</small>
                    </div>
                    <div class="feature-card">
                        <strong>⚙️ Hardware Design</strong>
                        <small>Actuators, sensors, embedded</small>
                    </div>
                </div>
                <div style="display: flex; gap: 1rem; justify-content: center; align-items: stretch; flex-wrap: wrap;">
                    <div class="feature-card">
                        <strong>🔌 Neural Networks</strong>
                        <small>ML, computer vision</small>
                    </div>
                    <div class="feature-card">
                        <strong>🎮 Simulation</strong>
                        <small>Gazebo, Webots analysis</small>
                    </div>
                    <div class="feature-card">
                        <strong>🤝 Swarm Intelligence</strong>
                        <small>Multi-robot coordination</small>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # --- CHAT AREA - Flexible Height ---
        current_chat = st.session_state.chats[st.session_state.current_chat_id]
        
        chat_container = st.container()
        with chat_container:
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            
            if not current_chat["messages"]:
                st.markdown("""
                <div class="welcome-message">
                    <div class="welcome-title">Welcome to RoboGPT</div>
                    <p>I'm your advanced robotics engineering assistant. Ask me about code debugging, autonomous navigation, hardware design, or any robotics-related topics.</p>
                    <p>Initiating neural connection... Ready for queries.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                for message in current_chat["messages"]:
                    if message["role"] == "user":
                        st.markdown(f'<div class="chat-message user-message"><strong>👤 User:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="chat-message bot-message"><strong>🤖 RoboGPT:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

    # --- INPUT AREA - Fixed at Bottom ---
    st.markdown('<div class="input-area">', unsafe_allow_html=True)
    with st.form(key="chat_input_form", clear_on_submit=True):
        col1, col2 = st.columns([10, 1])
        with col1:
            user_input = st.text_input(
                "Neural Interface Input:",
                placeholder="Enter your robotics query...",
                key="user_input",
                disabled=st.session_state.is_generating,
                label_visibility="collapsed"
            )
        with col2:
            submitted = st.form_submit_button(
                "⚡ Send",
                use_container_width=True,
                disabled=st.session_state.is_generating
            )
    st.markdown('</div>', unsafe_allow_html=True)
    
    if submitted and user_input:
        process_user_input(user_input)

def process_user_input(user_input):
    st.session_state.is_generating = True
    current_chat = st.session_state.chats[st.session_state.current_chat_id]
    current_chat["messages"].append({"role": "user", "content": user_input})
    
    # Auto-rename chat based on first message
    if len(current_chat["messages"]) == 1 and (current_chat["name"].startswith("New Chat") or current_chat["name"].startswith("Chat ")):
        # Create a short name from the first few words of the user input
        words = user_input.split()[:4]  # Take first 4 words
        new_name = " ".join(words)
        if len(new_name) > 30:
            new_name = new_name[:27] + "..."
        current_chat["name"] = new_name
    
    response_placeholder = st.empty()
    
    try:
        response_placeholder.markdown("""
        <div class="typing-indicator">
            <strong>🤖 RoboGPT:</strong><br>
            Initializing neural pathways...
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)
        
        response_placeholder.markdown("""
        <div class="typing-indicator">
            <strong>🤖 RoboGPT:</strong><br>
            Analyzing robotics parameters...
        </div>
        """, unsafe_allow_html=True)
        
        full_response = ""
        for chunk in st.session_state.robogpt.generate_streaming(user_input):
            full_response = chunk.strip()
            if full_response:
                response_placeholder.markdown(f"""
                <div class=\"chat-message bot-message\">
                    <strong>🤖 RoboGPT:</strong><br>
                    {full_response}
                </div>
                """, unsafe_allow_html=True)
            time.sleep(0.05)
            
        if full_response.strip():
            current_chat["messages"].append({"role": "assistant", "content": full_response})
            
    except Exception as e:
        st.error(f"Neural network error: {str(e)}")
        current_chat["messages"].append({
            "role": "assistant", 
            "content": f"Neural network encountered an error: {str(e)}. Please check system diagnostics."
        })
    finally:
        st.session_state.is_generating = False
        st.rerun()

if __name__ == "__main__":
    main()