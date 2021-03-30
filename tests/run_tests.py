from trisbm import trisbm
import unittest


class TriTest(unittest.TestCase):

    def test_import(self):
        model = trisbm()

    def test_make_graph(self):
        import pandas as pd
        import numpy as np

        df = pd.DataFrame(
            index = ["w_{}".format(w) for w in range(100)],
            columns = ["doc_{}".format(doc) for doc in range(25)],
            data = np.random.randint(0,10, size=2500).reshape((100,25
            ))            
        )

        model = trisbm()
        model.make_graph(df, lambda w: 1 if int(w.split("_")[1]) < 90 else 2)

    def test_fit(self):
        import pandas as pd
        import numpy as np

        df = pd.DataFrame(
            index=["w_{}".format(w) for w in range(100)],
            columns=["doc_{}".format(doc) for doc in range(25)],
            data=np.random.randint(0, 10, size=2500).reshape((100, 25
                                                              ))
        )

        model = trisbm()
        model.make_graph(df, lambda w: 1 if int(w.split("_")[1]) < 90 else 2)
        model.fit(verbose=False)

    def test_save(self):
        import pandas as pd
        import numpy as np

        df = pd.DataFrame(
            index=["w_{}".format(w) for w in range(100)],
            columns=["doc_{}".format(doc) for doc in range(25)],
            data=np.random.randint(0, 10, size=2500).reshape((100, 25
                                                              ))
        )

        model = trisbm()
        model.make_graph(df, lambda w: 1 if int(w.split("_")[1]) < 90 else 2)
        model.fit(verbose=False)
        model.save_data()


if __name__ == "__main__":
    unittest.main()
