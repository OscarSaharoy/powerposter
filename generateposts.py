import subprocess

with open("text-template.svg") as f:
    text_template = f.read()

def measure(text):
    populated_template = text_template.replace( "{{ text }}", text )

    output = subprocess.run(
        [ "inkscape", "--pipe", "--query-width", "--query-id=test-text" ],
        input=populated_template,
        capture_output=True,
        text=True,
    )

    return output

text = "test text"
print( measure(text) )
