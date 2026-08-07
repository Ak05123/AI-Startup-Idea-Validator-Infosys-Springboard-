from langchain_core.language_models.chat_models import BaseChatModel

from app.config import gemini_models


class GeminiFallbackModel(BaseChatModel):

    @property
    def _llm_type(self):
        return "gemini_fallback"

    def invoke(self, input, config=None, **kwargs):

        last_exception = None

        for index, model in enumerate(gemini_models, start=1):

            try:

                print(f"\nUsing Gemini API Key {index}")

                return model.invoke(
                    input,
                    config=config,
                    **kwargs
                )

            except Exception as e:

                print(
                    f"Gemini API Key {index} failed."
                )

                last_exception = e

                continue

        raise last_exception