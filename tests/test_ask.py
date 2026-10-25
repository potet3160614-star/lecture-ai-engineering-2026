"""ask.py の会話ループのテスト（Gemini API は呼ばない）。"""

import sys
from types import SimpleNamespace

from app import ask as ask_module


def test_main_keeps_follow_up_questions_in_one_chat(monkeypatch, capsys):
    class FakeChat:
        def __init__(self):
            self.questions = []

        def send_message(self, question):
            self.questions.append(question)
            return SimpleNamespace(text=f"回答: {question}", usage_metadata=None)

    chat = FakeChat()
    create_calls = []

    class FakeClient:
        def __init__(self, api_key):
            pass

        @property
        def chats(self):
            return self

        def create(self, model):
            create_calls.append(model)
            return chat

    monkeypatch.setattr(ask_module.genai, "Client", FakeClient)
    monkeypatch.setattr("app.ask.get_api_key", lambda: "test-key")
    monkeypatch.setattr(sys, "argv", ["app.ask", "最初の質問"])
    questions = iter(["続けて質問", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(questions))

    ask_module.main()

    output = capsys.readouterr().out
    assert chat.questions == ["最初の質問", "続けて質問"]
    assert create_calls == [ask_module.MODEL]
    assert "回答: 最初の質問" in output
    assert "回答: 続けて質問" in output
