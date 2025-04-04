import base64
import os
from google import genai
from google.genai import types

# will be called by the master file
def generateRoast(data): # take in the top 5 artists and songs data
    print("Generating Roast (WIP)")

    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Hello!"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Alright, let's do this. Lay it on me. Tell me your top artists and songs. Don't be shy, I'm ready to dissect your musical soul...and probably find some skeletons in its closet. Don't worry, I'll be gentle...ish. 😉
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
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

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

# if __name__ == "__main__":
#     generate()