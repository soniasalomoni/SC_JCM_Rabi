# --------------- #
# import packages #
# --------------- #

from hypothesis import strategies as st
from hypothesis import given
import sys

sys.path.append('.')

# --------------- #
# import classes  #
# --------------- #

from Classes.Field import Field

# ----------------------- #
# start property testing  #
# ----------------------- #

def is_PDF(pdf, N):
    """
    This function check if the function pdf is a Probability Density Function:
    - pdf(n) is non-negative for all possible values of n.
    - The sum of pdf(n) over all possible values of n is normalized.
    Because we're dealing with PDF of photons, n is a positive integer
    within the range [0,N].

    Parameters:
    -----------
    pdf : callable(n)
        the function we want to check
    N : int
        the maximum value for n

    """
    norm = 0
    for n in range(0,N):
        if pdf(n) < 0:
            return False
        norm = norm + pdf(n)
    if abs(norm-1) > 0.01:
        return False
    else:
        return True

@given(AVG_N = st.integers(0,50), PDF_N = st.just("Dirac"), CUT_N = st.integers(100,300))
def test_Dirac(AVG_N,PDF_N,CUT_N):
    field = Field(AVG_N,PDF_N,CUT_N)
    bool = is_PDF(field.Dirac,field.cut_n)
    assert(bool == True) , "Field.Dirac is not a PDF"

@given(AVG_N = st.integers(0,50), PDF_N = st.just("Poisson"), CUT_N = st.integers(100,300))
def test_Poisson(AVG_N,PDF_N,CUT_N):
    field = Field(AVG_N,PDF_N,CUT_N)
    bool = is_PDF(field.Poisson,field.cut_n)
    assert(bool == True) , "Field.Poisson is not a PDF"

@given(AVG_N = st.integers(0,20), PDF_N = st.just("BoseEinstein"), CUT_N = st.integers(100,300))
def test_BoseEinstein(AVG_N,PDF_N,CUT_N):
    field = Field(AVG_N,PDF_N,CUT_N)
    bool = is_PDF(field.BoseEinstein,field.cut_n)
    assert(bool == True) , "Field.BoseEinstein is not a PDF"








