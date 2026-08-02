from markitdown import MarkItDown

md = MarkItDown()

result = md.convert("input/sample.pdf")

with open("output/sample.md", "w", encoding="utf-8") as file:
    file.write(result.text_content)

print("Conversion completed")