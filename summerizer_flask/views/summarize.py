from services.models.summarizer_model import summarize_text
from flask import (
    Blueprint,
    request,
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint("summ", __name__, url_prefix="/summ")


@bp.route("/", methods=["get"])
def summarizer():
    """
    recieve text in body of request::
        payload={'text': 'sample text'}
        response = requests.request("GET", url, data=payload)

    responses:
        200:
         description: "summerizetion DONE!"
        422:
         description: if language is unsupported/mix"
        500:
         description: enternal error
    """
    try:
        text = request.form["text"]
        result = summarize_text(text=text)
        if isinstance(result, dict):
            return result, 200
        else:
            return {"error": result}, 422
    except Exception as e:
        return {"error": str(e)}, 500
