import apiaudio
#
#
apiaudio.api_key = "API_KEY"

audience_params = [
    {"deal": "Bonus Cash", "model": "Expedition", "location": "Mid-South" },
]

# Add your script text
scriptText = """
<<soundSegment::main>>
<<sectionName::main>>
<<media::mazdavo>>
<<soundSegment::*>>
<<sectionName::main2>>
Now, get 0 percent APR financing for 72 months, plus {{deal}} on Ford {{model}}. Only at your {{location}} Ford Dealer.
"""

# Add your personalized parameters to script.create, speech create and mastering
for audience in audience_params:

    # Script template
    script = apiaudio.Script.create(scriptText=scriptText)
    print("mazda", script)

    # Retrieves scriptID
    script = apiaudio.Script.retrieve(scriptId=script["scriptId"])
    print(script)

    # Force your sections length
    sectionProperties = {
        'main': {'endAt': 21.1, 'justify': 'flex-start'},
        'main2': {'endAt': 31, 'justify': 'flex-start'},
    }
        
    # Creates text to speech
    r = apiaudio.Speech().create(
    scriptId=script["scriptId"],
    voice="sara",
    speed=115,
    silence_padding=0,
    sectionProperties=sectionProperties,
    audience=audience,
    )

    # Add all parameters to the response
    template = "demo"
    response = apiaudio.Mastering().create(
    scriptId=script.get("scriptId"),
    soundTemplate=template,
    audience=audience,
    forceLength=31.0,
    mediaFiles = [{"mazdavo":"2a72a6a1"}],
    sectionProperties=sectionProperties,
    )

    print(response)
    file = apiaudio.Mastering().download(
    scriptId=script.get("scriptId"), parameters=audience, destination=".")
    print(file)