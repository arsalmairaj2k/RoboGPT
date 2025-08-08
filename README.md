# RoboGPT
# 🤖 RoboGPT - AI Assistant

> **Advanced Robotics Engineering Assistant powered by Google Gemini AI**

RoboGPT is a sophisticated AI-powered chatbot specifically designed for robotics engineering and development. It provides expert assistance across the entire robotics development pipeline, from code debugging to hardware design and simulation analysis.

![RoboGPT Interface](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-orange)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-purple)

<img width="1864" height="890" alt="Screenshot from 2025-08-08 15-08-42" src="https://github.com/user-attachments/assets/28929cc6-4f66-4531-811b-05bd91866344" />


## ✨ Features

### 🧠 **Core Capabilities**
- **🔧 Code Analysis**: C/C++, Python, ROS debugging and optimization
- **🧭 Navigation AI**: SLAM, path planning, autonomous systems
- **⚙️ Hardware Design**: Actuators, sensors, embedded systems
- **🔌 Neural Networks**: Machine learning, computer vision
- **🎮 Simulation**: Gazebo, Webots, PyBullet analysis
- **🤝 Swarm Intelligence**: Multi-robot coordination systems

### 🎨 **User Interface**
- **Futuristic Design**: Modern, sci-fi inspired UI with neural network aesthetics
- **Real-time Streaming**: Typewriter effect for AI responses
- **Responsive Layout**: Works on desktop and mobile devices
- **Interactive Elements**: Floating particles, animated backgrounds
- **Dark Theme**: Easy on the eyes for extended coding sessions

### 🔧 **Technical Features**
- **Dual Interface**: Streamlit web app + FastAPI backend
- **Streaming Responses**: Real-time AI response generation
- **Session Management**: Persistent chat history
- **API Integration**: Google Gemini 2.5 Flash model
- **Error Handling**: Robust error management and recovery

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/RoboGPT.git
   cd RoboGPT
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv robogpt_env
   source robogpt_env/bin/activate  # On Windows: robogpt_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file in the RoboGPT directory
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   # For Streamlit interface (recommended)
   streamlit run streamlitapp.py
   
   # For FastAPI backend
   python main.py
   ```

## 📁 Project Structure

```
RoboGPT/
├── streamlitapp.py     # Main Streamlit web application
├── RoboGPT.py          # Core AI logic and Gemini integration
├── main.py             # FastAPI backend server
├── UI.css              # Custom CSS styling
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .env               # Environment variables (create this for your LLM APLI key)
```

## 🎯 Usage

### Streamlit Interface (Recommended)

1. **Start the app**: `streamlit run streamlitapp.py`
2. **Open your browser**: Navigate to `http://localhost:8501`
3. **Ask questions**: Type your robotics queries in the input field
4. **Get responses**: Watch as RoboGPT streams its responses in real-time

### Example Queries

- *"How do I implement SLAM for a mobile robot using ROS?"*
- *"Debug this Arduino code for motor control"*
- *"What sensors should I use for autonomous navigation?"*
- *"Help me optimize this path planning algorithm"*
- *"How do I set up a multi-robot simulation in Gazebo?"*

### FastAPI Backend

The FastAPI server provides a REST API for integration with other applications:

```bash
# Start the server
python main.py

# API endpoints
GET  /                    # Health check
POST /generate           # Generate AI response
```

**Example API call:**
```python
import requests

response = requests.post("http://localhost:8000/generate", 
                        json={"user_prompt": "How do I implement SLAM?"})
print(response.json()["response"])
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### Customization

- **UI Styling**: Modify `UI.css` for custom appearance
- **AI Behavior**: Edit the system prompt in `RoboGPT.py`
- **Model Selection**: Change the model in `RoboGPT.py` (default: `gemini-2.5-flash`)

## 🛠️ Development

### Adding New Features

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Local Development

```bash
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
streamlit run streamlitapp.py --server.runOnSave true

# Run tests (if available)
python -m pytest tests/
```

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file contains the correct `GEMINI_API_KEY`
   - Verify the API key is valid and has sufficient quota

2. **Sidebar Not Visible**
   - Press `S` on your keyboard to toggle the sidebar
   - Use the hamburger menu (☰) button
   - Refresh the page if needed

3. **Slow Response Times**
   - Check your internet connection
   - Verify the Gemini API is responding
   - Consider upgrading your API plan

4. **UI Not Loading**
   - Clear browser cache
   - Try incognito/private browsing mode
   - Check browser console for errors

### Debug Mode

Enable debug mode by adding debug statements:

```python
# In streamlitapp.py
st.write("Debug: Processing input...")
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### How to Contribute

1. **Report bugs** using GitHub Issues
2. **Suggest features** via GitHub Discussions
3. **Submit pull requests** for improvements
4. **Improve documentation** and examples

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the underlying AI model
- **Streamlit** for the web framework
- **FastAPI** for the backend API
- **Open Source Community** for various libraries and tools

## 📞 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/yourusername/RoboGPT/issues)
- **Discussions**: [Join the community](https://github.com/yourusername/RoboGPT/discussions)
- **Email**: your.email@example.com

## 🔄 Version History

- **v4.0** - Current version with streaming responses and futuristic UI
- **v3.0** - Added FastAPI backend and improved error handling
- **v2.0** - Enhanced UI with custom CSS and animations
- **v1.0** - Initial release with basic Streamlit interface

---

**Made with ❤️ for the Robotics Community**

*RoboGPT - Your AI-powered robotics engineering companion*
