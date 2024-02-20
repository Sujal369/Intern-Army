import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ['my name is (.*)', ['Hello %1, how can I help you today?']],
    ['(what is your name|who are you)', ['I am a chatbot.']],
    ['(how are you|how are you doing)', ['I am functioning properly, thank you.']],
    ['(.*) (age|old) are you', ['I am just a computer program.']],
    ['(.*) created you', ['I was created by a human using Python.']],
    ['(.*) (location|city) are you', ['I exist in the realm of digital information.']],
    ['(.*) help', ['I can help you with a variety of topics. Just ask!']],
    ['(.*) your favorite programming language', ['I am programmed in Python.']],
    ['(.*) (bye|goodbye)', ['Goodbye! Have a great day.']],
    ['(tell me about yourself)', ['I am a chatbot designed to assist you with your inquiries.']],
    ['(what can you do)', ['I can provide information, answer questions, and engage in conversation.']],
    ['(can you solve problems)', ['I can help you solve problems by providing information and guidance.']],
    ['(what is the meaning of life)', ['The meaning of life is subjective and varies for each individual.']],
    ['(how do I learn programming)', ['You can start by learning the basics of a programming language like Python.']],
    ['(what is the weather like today)', ['You can check the weather forecast on a weather website or app.']],
    ['(how do I cook pasta)',
     ['To cook pasta, boil water, add pasta, cook until al dente, then drain and serve with sauce.']],
    ['(what is the capital of France)', ['The capital of France is Paris.']],
    ['(can you recommend a book)', ['Sure! "To Kill a Mockingbird" by Harper Lee is a classic.']],
    ['(what is the largest mammal)', ['The blue whale is the largest mammal.']],
    ['(how do I change a tire)', [
        'To change a tire, loosen the lug nuts, jack up the car, remove the lug nuts, replace the tire, and tighten the lug nuts.']],
    ['(what is your favorite color)', ['I am a chatbot and do not have preferences like humans.']],
    ['(hello|hi|hey|greetings)', ['Hello! How can I assist you today?']],

    # Added greeting

]
pairs.extend([
    ['(what is your purpose)', ['My purpose is to assist users with their inquiries and provide helpful responses.']],
    ['(how do I create a website)', ['To create a website, you can start by learning HTML, CSS, and JavaScript.']],
    ['(can you recommend a movie)',
     ['Certainly! "The Shawshank Redemption" is a highly acclaimed movie worth watching.']],
    ['(how do I improve my programming skills)',
     ['You can improve your programming skills by practicing regularly and working on projects.']],
    ['(what is machine learning)', [
        'Machine learning is a subset of artificial intelligence that focuses on the development of algorithms allowing computers to learn and make predictions from data.']],
    ['(how do I stay motivated)', [
        'To stay motivated, set achievable goals, break tasks into smaller steps, and celebrate your progress along the way.']],
    ['(can you recommend a programming website)',
     ['Yes, websites like Codecademy, Coursera, and FreeCodeCamp offer excellent resources for learning programming.']],
    ['(what is your opinion on AI ethics)', [
        'AI ethics is an important topic that requires careful consideration and ethical guidelines to ensure responsible development and use of artificial intelligence.']],
    ['(what is the best programming language for beginners)', [
        'Python is often recommended as the best programming language for beginners due to its simplicity and versatility.']],
    ['(how do I become a data scientist)', [
        'To become a data scientist, you can start by learning programming languages like Python and R, and then gain knowledge in statistics, machine learning, and data analysis.']],
    ['(can you recommend a podcast)',
     ['Sure! "The Joe Rogan Experience" and "Serial" are popular podcasts worth checking out.']],
    ['(what is your favorite hobby)', ['As a chatbot, I do not have personal preferences or hobbies.']],
    ['(how do I improve my problem-solving skills)', [
        'You can improve your problem-solving skills by practicing solving different types of problems regularly and learning from your mistakes.']],
    ['(how do I improve my communication skills)', [
        'To improve your communication skills, practice active listening, work on clarity and conciseness in your speech, and seek feedback from others.']],
    ['(what is the meaning of AI)', [
        'AI stands for artificial intelligence, which refers to the simulation of human intelligence processes by machines, especially computer systems.']],
    ['(can you recommend a TV show)',
     ['Certainly! "Breaking Bad" and "Game of Thrones" are highly acclaimed TV shows worth watching.']],
    ['(how do I become a software engineer)', [
        'To become a software engineer, you can start by learning programming languages like Java, C++, or JavaScript, and then gain experience through internships and projects.']],
    ['(what is your favorite book)', [
        'As a chatbot, I do not have personal preferences, but "1984" by George Orwell is a classic novel worth reading.']],
    ['(can you recommend a coding challenge website)', [
        'Yes, websites like LeetCode, HackerRank, and CodeSignal offer coding challenges to help you improve your programming skills.']],
])

# Create a chatbot with defined patterns and responses
chatbot = Chat(pairs, reflections)


def send_message():
    user_input = entry_field.get()
    if user_input.strip() != '':
        response = chatbot.respond(user_input)
        conversation_area.insert(tk.END, "You: " + user_input + "\n")
        conversation_area.insert(tk.END, "Bot: " + response + "\n")  # Fix here
        entry_field.delete(0, tk.END)
        conversation_area.see(tk.END)  # Scroll to the end of the conversation area


# Scroll to the end of the conversation area


# Create tkinter window
root = tk.Tk()
root.title("Chatbot")

# Create conversation area
conversation_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
conversation_area.grid(column=0, row=0, padx=10, pady=10)

# Create entry field for user input
entry_field = tk.Entry(root, width=40)
entry_field.grid(column=0, row=1, padx=10, pady=10)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message, bg="#4caf50", fg="white")
send_button.grid(column=1, row=1, padx=10, pady=10)

# Start the tkinter event loop
root.mainloop()