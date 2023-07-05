import pytest

from PageObjects.Relationship_Menu_Objects import Relationship_Objects
from PageObjects.Selectable_Menu_Objects import Selectable_Objects
from PageObjects.Table_With_Cheakbox_Menu_Objects import Table_With_Cheakbox_Objects
from PageObjects.Tootip_Menu_Objects import Tooltip_Objects
from Utilities.Excel_File import Excel_File_Opractions
from Utilities.Logger import Log_Opractions


class Test:
    log = Log_Opractions.getLogs()
    Excel = Excel_File_Opractions()

    @pytest.mark.Relationship
    def test_relationship(self, setup):
        self.log.info("Test Relationship is Started")
        self.driver = setup
        self.log.info("Invoking Browser and Opening URL")
        R = Relationship_Objects(self.driver)

        R.relationship()
        self.log.info("Clicking on Relationship Button")
        R.grand_parent1(self.Excel.read_excel(3, 1))
        self.log.info(f"Entering Grand Parent-1 Details as: {self.Excel.read_excel(3, 1)}")
        R.parent1(self.Excel.read_excel(3, 2))
        self.log.info(f"Entering Parent-1 Details as: {self.Excel.read_excel(3, 2)}")
        R.child1(self.Excel.read_excel(3, 3))
        self.log.info(f"Entering Child-1 Details as: {self.Excel.read_excel(3, 3)}")

        R.grand_parent2(self.Excel.read_excel(3, 4))
        self.log.info(f"Entering Grand Parent-2 Details as: {self.Excel.read_excel(3, 4)}")
        R.parent2(self.Excel.read_excel(3, 5))
        self.log.info(f"Entering Parent-2 Details as: {self.Excel.read_excel(3, 5)}")
        R.child2(self.Excel.read_excel(3, 6))
        self.log.info(f"Entering Child-2 Details as: {self.Excel.read_excel(3, 6)}")
        R.status("Relationship")
        self.log.info("Status of The Page is Captured")
        self.driver.close()
        self.log.info("Test Relationship is Completed")
    # ------------------------------------------

    @pytest.mark.Tooltip
    def test_tooltip(self, setup):
        self.log.info("Test Tooltip is Started")
        self.driver = setup
        self.log.info("Invoking Browser and Opening URL")
        T = Tooltip_Objects(self.driver)
        R = Relationship_Objects(self.driver)

        T.tooltip()
        self.log.info("Clicking on Tooltip Button")
        T.name(self.Excel.read_excel(7, 1))
        self.log.info(f"Entering Name as: {self.Excel.read_excel(7, 1)}")
        T.surname(self.Excel.read_excel(7, 2))
        self.log.info(f"Entering Surname as: {self.Excel.read_excel(7, 2)}")
        T.address(self.Excel.read_excel(7, 3))
        self.log.info(f"Entering Address as: {self.Excel.read_excel(7, 3)}")
        R.status("Tooltip")
        self.log.info("Status of The Page is Captured")
        self.driver.close()
        self.log.info("Test Tooltip is Completed")
    # ------------------------------------------

    @pytest.mark.skip("Under Devlopment")
    def test_iframe(self, setup):
        pass
    # ------------------------------------------

    @pytest.mark.Table_With_Cheakbox
    def test_table_with_cheakbox(self, setup):
        self.log.info("Test Table With Cheakbox is Started")
        self.driver = setup
        self.log.info("Invoking Browser and Opening URL")
        T1 = Table_With_Cheakbox_Objects(self.driver)
        R = Relationship_Objects(self.driver)

        T1.table_with_cheakbox()
        self.log.info("Clicking on Table With Cheakbox Option")
        T1.cat()
        self.log.info("Clicking on Cat Option")
        T1.dog()
        self.log.info("Clicking on Dog Option")
        T1.cow()
        self.log.info("Clicking on Cow Option")
        T1.lion()
        self.log.info("Clicking on Lion Option")
        T1.tiger()
        self.log.info("Clicking on Tiger Option")
        R.status("Table_With_Cheakbox")
        self.log.info("Status of The Page is Captured")
        self.driver.close()
        self.log.info("Test Table With Cheakbox is Completed")
    # ------------------------------------------

    @pytest.mark.Selectable
    def test_selectable(self, setup):
        self.driver = setup
        S = Selectable_Objects(self.driver)

        S.selectable()
        S.items()