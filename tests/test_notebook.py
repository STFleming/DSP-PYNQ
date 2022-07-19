from pynq import Overlay
from pynqutils.runtime import run_notebook, NotebookResult
import os


class CannotFindNotebook(Exception):
    pass

def test_notebook():
    """ Tests the helloworld notebook to see that it executes correctly """
    jupyter_notebooks = os.getenv('PYNQ_JUPYTER_NOTEBOOKS')

    # Try and find the notebook
    if os.path.isdir(f"{jupyter_notebooks}/dsp-pynq"):
        if os.path.isfile(f"{jupyter_notebooks}/dsp-pynq/02_dsp_and_pynq.ipynb"): 
            result = run_notebook(f"{jupyter_notebooks}/dsp-pynq/02_dsp_and_pynq.ipynb")
        else:
            raise CannotFindNotebook(f"unable to locate the helloworld notebook, expecting it at {jupyter_notebooks}/dsp-pynq/02_dsp_and_pynq.ipynb")
    else:
        raise CannotFindNotebook(f"unable to locate the helloworld directory, expecting it at {jupyter_notebooks}/dsp-pynq")



