def load_template(template_path):

    with open(template_path, "r", encoding="utf-8") as file:
        return file.read()

def personalize_template(template, name, task):

    message = template.replace("{name}", name)
    message = message.replace("{task}", task)

    return message