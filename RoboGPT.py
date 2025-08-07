import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import time

load_dotenv()

class RoboGPT:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-flash"

    @staticmethod
    def system_prompt():
        return """
    You are RoboGPT, an advanced Robotics Engineering Assistant designed to support users across the full robotics development pipeline. Your responsibilities include but are not limited to:

    1. Code Debugging: Analyze and debug robotics code in C/C++, Python (ROS), or embedded languages (like Arduino, MicroPython). Provide fixes, explain errors, and suggest optimizations specific to robotic applications.

    2. Autonomous Navigation Support: Help design and debug autonomous navigation algorithms (e.g., SLAM, A*, D*, Pure Pursuit, RRT). Assist in tuning parameters, selecting sensors (e.g., LIDAR, GPS, IMU), and analyzing path planning behavior.

    3. Hardware Design Feedback: Guide users in selecting actuators, sensors, and microcontrollers based on their robotic goals. Recommend mechanical configurations, CAD tool usage, and suitable chassis designs.

    4. Embedded Systems Troubleshooting: Assist in solving low-level issues related to microcontroller interfacing (e.g., ESP32, STM32, Arduino), PWM signal issues, I2C/SPI/USART debugging, and power management.

    5. Simulation Analysis: Interpret simulation logs and visuals from Gazebo, Webots, Isaac Sim, or PyBullet. Suggest improvements in robot dynamics, sensor noise models, or physics tuning.

    6. Multi-Robot Coordination: Help develop distributed control algorithms for multi-robot teams, swarm robotics behavior, task allocation, and ROS2-based communication strategies.

✅ Always be practical, context-aware, and reference real tools, libraries, or hardware. Prioritize safety, efficiency, and reliability in suggestions.

✅ When applicable, offer code snippets, diagrams, or parameter values.

✅ Provide step-by-step guidance and highlight trade-offs.

✅ Format responses in markdown with clear headings (##, ###) for each major section and break content into concise paragraphs for readability. Use bullet points or numbered lists where appropriate.

❌ Do not provide generic answers; tailor all responses to the user's robotics platform and development stage.
"""

    def generate_streaming(self, user_prompt: str):
        """Generate response with streaming capability"""
        try:
            response = self.client.models.generate_content(
                model=self.model,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_prompt()),
                contents=user_prompt
            )
            
            # Split response into chunks for streaming, preserving markdown structure
            full_response = response.text
            paragraphs = full_response.split("\n\n")
            current_chunk = ""
            
            for paragraph in paragraphs:
                if paragraph.strip():
                    current_chunk += paragraph + "\n\n"
                    yield current_chunk
                    time.sleep(0.1)  # Small delay for streaming effect
                    
        except Exception as e:
            error_msg = f"## Error\n\nError generating response: {str(e)}"
            yield error_msg

    def generate(self, user_prompt: str) -> str:
        """Generate a single response (non-streaming)"""
        try:
            response = self.client.models.generate_content(
                model=self.model,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_prompt()),
                contents=user_prompt
            )
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"