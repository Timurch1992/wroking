# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: PetCare
import unittest
from petcare import PetCare


class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.pc = PetCare("Рекс", 5, "собака")

    def test_empty_log(self):
        self.assertEqual(self.pc.get_logs(), [])

    def test_log_single(self):
        self.pc.log("Поедал 100г")
        self.assertEqual(self.pc.get_logs(), ["Поедал 100г"])

    def test_log_multiple(self):
        self.pc.log("Поедал 100г")
        self.pc.log("Гулял 30 мин")
        self.assertEqual(self.pc.get_logs(), ["Поедал 100г", "Гулял 30 мин"])

    def test_log_empty_string(self):
        self.pc.log("")
        self.assertEqual(self.pc.get_logs(), [""])

    def test_log_whitespace(self):
        self.pc.log("   ")
        self.assertEqual(self.pc.get_logs(), ["   "])

    def test_log_unicode(self):
        self.pc.log("🐶 🍖 🚶")
        self.assertEqual(self.pc.get_logs(), ["🐶 🍖 🚶"])

    def test_log_mixed(self):
        self.pc.log("Поедал 100г")
        self.pc.log("   ")
        self.pc.log("Гулял 30 мин")
        self.pc.log("🐶 🍖 🚶")
        self.assertEqual(self.pc.get_logs(), ["Поедал 100г", "   ", "Гулял 30 мин", "🐶 🍖 🚶"])

    def test_log_special_chars(self):
        self.pc.log('Test "quotes" & symbols!@#$%^&*()')
        self.assertEqual(self.pc.get_logs(), ['Test "quotes" & symbols!@#$%^&*()'])

    def test_log_long_string(self):
        long_str = "A" * 1000
        self.pc.log(long_str)
        self.assertEqual(self.pc.get_logs(), [long_str])

    def test_log_with_newline(self):
        self.pc.log("Line1\nLine2")
        self.assertEqual(self.pc.get_logs(), ["Line1\nLine2"])

    def test_log_tab(self):
        self.pc.log("Line1\tLine2")
        self.assertEqual(self.pc.get_logs(), ["Line1\tLine2"])

    def test_log_newline_only(self):
        self.pc.log("\n")
        self.assertEqual(self.pc.get_logs(), ["\n"])

    def test_log_tab_only(self):
        self.pc.log("\t")
        self.assertEqual(self.pc.get_logs(), ["\t"])

    def test_get_logs_after_empty(self):
        self.assertEqual(self.pc.get_logs(), [])

    def test_get_logs_after_single(self):
        self.pc.log("Поедал 100г")
        self.assertEqual(self.pc.get_logs(), ["Поедал 100г"])

    def test_get_logs_after_multiple(self):
        self.pc.log("Поедал 100г")
        self.pc.log
