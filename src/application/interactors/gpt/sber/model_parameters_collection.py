from application.interactors.gpt.sber.request_containers import ModelParameters, ModelTypes

PRO_NON_CREATIVE = ModelParameters(
    model=ModelTypes.GIGACHAT_PRO,
    temperature=0.01,
    top_p=0.01,
    n=1,
    stream=False,
    max_tokens=1024,
    repetition_penalty=1.0,
)

LITE_PLUS_NON_CREATIVE = ModelParameters(
    model=ModelTypes.GIGACHAT_LITE_PLUS,
    temperature=0.01,
    top_p=0.01,
    n=1,
    stream=False,
    max_tokens=10000,
    repetition_penalty=1.0,
)

LITE_NON_CREATIVE = ModelParameters(
    model=ModelTypes.GIGACHAT_LITE,
    temperature=0.01,
    top_p=0.1,
    n=1,
    stream=False,
    max_tokens=1024,
    repetition_penalty=1.0,
)
