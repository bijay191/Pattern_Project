from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def refine_regex(file_list, rough_regex):
    input_text = f"""
    Generate a clean regex for:
    {", ".join(file_list)}

    Improve:
    {rough_regex}

    Return only regex.
    """

    inputs = tokenizer(input_text, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=64)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)