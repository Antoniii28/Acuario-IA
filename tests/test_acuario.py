import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from acuario_ia import monitorear, buscar, heuristica, INICIAL, META, sucesores

class TestAcuario(unittest.TestCase):
    def test_monitoreo_normal(self): self.assertEqual(monitorear("Normal",25,35,8.2), [])
    def test_alertas(self): self.assertEqual(len(monitorear("Mal",28,38,7.8)), 3)
    def test_meta(self): self.assertEqual(heuristica(META), 0)
    def test_bfs(self): self.assertEqual((len(buscar("BFS")[0]),buscar("BFS")[1]), (3,20))
    def test_optimo(self): self.assertEqual((buscar("UCS")[1],buscar("A*")[1]), (13,13))
    def test_sucesores(self): self.assertTrue(all(c>0 for _,c,_ in sucesores(INICIAL)))

if __name__ == "__main__": unittest.main()
