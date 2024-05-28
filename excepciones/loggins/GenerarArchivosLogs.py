import logging
import traceback
import contextlib

logging.basicConfig(level=logging.DEBUG,
                    filename="errors.log",
                    format="%(asctime)s - %(levelname)s - %(message)s"
                    )


def write_on_log_file(error):
    exception_info = {
        "message": str(error),
        "detail": traceback.format_exc()
    }
    logging.error(exception_info)


try:
    10 / 0
except Exception as error:
    # ESTA FUNCION NOS DÁ TODA LA INFORMACIÓN DEL ERROR, PERO NO LA CAUSA.
    write_on_log_file(error)


@contextlib.contextmanager
def write_on_log_file_with_context():
    try:
        yield
    except Exception as error:
        exception_info = {
            "message": str(error),
            "detail": traceback.format_exc()
        }
        logging.error(exception_info)


# ESTA FUNCION NOS DÁ TODA LA INFORMACIÓN DEL ERROR Y SU CONTEXTO.
with write_on_log_file_with_context():
    var = 10 / 0
