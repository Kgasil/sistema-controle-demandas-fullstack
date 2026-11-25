import tempfile
import unittest
from pathlib import Path
import app as module


class DemandAPITest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.original_db = module.DB_NAME
        module.DB_NAME = Path(self.tmp.name) / "test.db"
        module.init_db()
        self.client = module.app.test_client()

    def tearDown(self):
        module.DB_NAME = self.original_db
        self.tmp.cleanup()

    def test_create_and_update(self):
        response = self.client.post("/api/demandas", json={
            "titulo": "Teste", "area": "Dados", "custo_estimado": 42,
        })
        self.assertEqual(response.status_code, 201)
        ident = response.get_json()["id"]
        self.assertEqual(self.client.patch(
            f"/api/demandas/{ident}/status", json={"status": "Concluído"}
        ).status_code, 200)
        rows = self.client.get("/api/demandas").get_json()
        self.assertEqual(rows[0]["status"], "Concluído")

    def test_invalid_payloads(self):
        for payload in [
            [], {"titulo": "A", "area": "B", "custo_estimado": -1},
            {"titulo": "A", "area": "B", "custo_estimado": "nan"},
            {"titulo": "A", "area": "B", "status": "Outro"},
        ]:
            with self.subTest(payload=payload):
                self.assertEqual(self.client.post(
                    "/api/demandas", json=payload
                ).status_code, 400)

    def test_missing_demand(self):
        self.assertEqual(self.client.patch(
            "/api/demandas/999/status", json={"status": "Concluído"}
        ).status_code, 404)


if __name__ == "__main__":
    unittest.main()
