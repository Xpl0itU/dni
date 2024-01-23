from src.tablaAsignacion import TablaAsignacion


def test_cases_tabla_ok():
    tabla = TablaAsignacion()

    casosTest = [  # casos test OK
        "78484464T",
        "72376173A",
        "01817200Q",
        "95882054E",
        "63587725Q",
        "26861694V",
        "21616083Q",
        "26868974Y",
        "40135330P",
        "89044648X",
        "80117501Z",
        "34168723S",
        "76857238R",
        "66714505S",
        "66499420A",
    ]
    for dni in casosTest:
        assert tabla.calcularLetra(dni[:-1]) == dni[-1]
