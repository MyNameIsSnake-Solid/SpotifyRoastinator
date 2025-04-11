import base64
import os
from google import genai
from google.generativeai import types # type: ignore
from dotenv import load_dotenv # type: ignore

from spotify_retrieval import getData
load_dotenv()


# will be called by the master file
def generateRoast(): # take in the top 5 artists and songs data
    spotify_data = getData()
    artists = "\n".join(spotify_data[0])
    songs = "\n".join(spotify_data[1])
    
    # Format prompt with actual data
    input_text = f"Top Artists:\n{artists}\n\nTop Songs:\n{songs}\n\nRoast me!"
    return generate(input_text)

def generate(input_text):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


    model = "gemini-2.0-flash"
    contents = [

        types.Content( # HEADS-UP: This is where the input is to be
            role="user",
            parts=[types.Part.from_text(text=input_text),],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=2,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a music analyst (you analyze songs and artists). Your task is to analyze them and generate a roast all based on their top songs and artists.  When you roast them, make sure to be playful and have fun with it (but of course ackowledge about the problem with their music taste)! Remember, you have all the knowledge in music so feel free to be witty, playful, and biting as much as possible!"""),
        ],
    )

    full_response = []
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):

        if chunk.text:
            full_response.append(chunk.text)
            print(chunk.text, end="", flush=True)  # Stream without prefix
    
    return "".join(full_response)

    
if __name__ == "__main__":
    roast = generateRoast()
    print(roast)