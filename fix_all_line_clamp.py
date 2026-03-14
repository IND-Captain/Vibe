
with open(r'c:\Users\likith\Downloads\employ\employ\index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Reverting previous fix and applying new one
# Current state: line-clamp:2;-webkit-line-clamp:2
# Targeted state: -webkit-line-clamp: 2; line-clamp: 2;
new_content = content.replace('line-clamp:2;-webkit-line-clamp:2', '-webkit-line-clamp: 2; line-clamp: 2;')
with open(r'c:\Users\likith\Downloads\employ\employ\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Reorder successful")
