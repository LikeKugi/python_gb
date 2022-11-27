from dataclasses import dataclass


@dataclass
class Answer:
    user_id: int = 0
    message_id: int = 0
    question_text: str = "Unknown"
    answer_text: str = "Unknown"