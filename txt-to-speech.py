from gradio_client import Client
from PIL import Image
import os
import webbrowser

# Connect to the Hugging Face Space
client = Client("NihalGazi/Text-To-Speech-Unlimited")

a = input("Enter the emotional style you want to use(e.g: excited, happy, calm, sad, etc.): ").strip().lower()
b = input("Enter the voice you want to use(alloy/echo/fable/onyx/shimmerballad): ").strip().lower()
c = input("Enter the text you want to hear: ").strip().lower()



def synthesize_text(
    prompt: str,
    voice: str = "alloy",
    emotion: str = "neutral",
    use_random_seed: bool = True,
    specific_seed: int = 12345
):
    result = client.predict(
        prompt,
        voice,
        emotion,
        use_random_seed,
        specific_seed,
        api_name="/text_to_speech_app"  # ✅ correct API endpoint
    )
    audio_path, status = result
    return audio_path, status

if __name__ == "__main__":
    prompt = c
    voice = b     # choose from the list provided in your API info
    emotion = a

    audio_path, status = synthesize_text(prompt, voice, emotion)
    print("Status:", status)
    print("Audio saved at:", audio_path)

    # Optional: play the audio
    if os.path.exists(audio_path):
        webbrowser.open(audio_path)
    else:
        print("Audio file not found.")
