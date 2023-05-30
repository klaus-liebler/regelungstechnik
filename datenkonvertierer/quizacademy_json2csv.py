import json
import csv
import os

# Pfad zur unformatierten .json-Datei (mit r-Präfix)
json_file = r"./datenkonvertierer/rt03.json"

# Extrahieren des Dateinamens ohne Erweiterung
file_name = os.path.splitext(json_file)[0]

# Laden der .json-Datei
with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extrahieren von Fragen, Antwortmöglichkeiten und korrekten Antworten
questions = data['questions']

# Funktion zum Markieren der korrekten Antwort
def mark_correct_answer(answers):
    for answer in answers:
        if answer['is_right']:
            answer['text'] = answer['text'] + " (Richtig)"
    return answers

# Erstellen der .csv-Datei
csv_file = f'{file_name}.csv'

# Ersetzung der Sonderzeichen
def replace_special_characters(text):
    replacements = {
        'ä': 'ae',
        'ö': 'oe',
        'ß': 'ss'
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    
    for question in questions:
        question_text = replace_special_characters(question['text'])
        answers = question['answers']
        marked_answers = mark_correct_answer(answers)
        
        # Schreiben der Frage
        writer.writerow([question_text])
        
        # Schreiben der Antwortmöglichkeiten
        for answer in marked_answers:
            answer_text = replace_special_characters(answer['text'])
            writer.writerow(['', answer_text])
        
        # Hinzufügen eines Absatzes
        writer.writerow([])
        
print(f"Die .csv-Datei '{csv_file}' wurde erfolgreich erstellt.")