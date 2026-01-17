def build_prompt(user_input, language):
    return f"""
    Write clean and correct {language} code.

    Task:
    {user_input}

    Requirements:
    - Correct syntax
    - Use best practices
    - Add comments
    """
