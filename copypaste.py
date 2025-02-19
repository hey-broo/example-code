import google.generativeai as genai
#pip install -q -U google-generativeai
model = genai.GenerativeModel('gemini-1.5-flash')

GOOGLE_API_KEY="AIzaSyDvOKzn7mBMKjKm3K1m5mbVZTRVqR_Uu38"

genai.configure(api_key=GOOGLE_API_KEY)

def prompt():
    input_h=input("you : ")
    response = model.generate_content(input_h)
    print(response.text)
    return response

#https://ai.google.dev/tutorials/python_quickstart

if __name__ == "__main__":
    while True:
        prompt()