"""About Page rendered with html/about_page.html text."""

# Copyright (C) 2023 Dennis Lönard
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pathlib

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTextBrowser, QVBoxLayout, QWidget

from src.img.img_path import img_path


class AboutPage(QWidget):
    """About Page rendered with html/about_page.html text."""

    def __init__(self) -> None:
        """About Page rendered with html/about_page.html text."""
        super().__init__()
        self.icon_dir = img_path()
        self.setWindowTitle("About Page")
        self.setMinimumSize(700, 500)
        self.setWindowIcon(QIcon(str(pathlib.Path(self.icon_dir, "about.svg"))))

        layout = QVBoxLayout()
        text = QTextBrowser(self)
        text.setOpenExternalLinks(True)
        text.setHtml(self.html_contents())
        layout.addWidget(text)
        self.setLayout(layout)
        self.show()

    @staticmethod
    def html_contents() -> str:
        """Return html content of help page."""
        # Baked into Python code here, so that it is inside the frozen executable, and we don't have to search for the
        # file path

        return (
            "<h1>HDF5 Viewer</h1>"
            "The source code for this HDF5 File Viewer can be found on "
            '<a href="https://github.com/loenard97/hdf5-viewer">GitHub</a>.'
            "<h2>Acknowledgements and Licenses</h2>"
            "The following Python libraries are used in this project:"
            "<ul>"
            '<li><a href="https://riverbankcomputing.com/commercial/pyqt">PyQt6</a></li>'
            '<li><a href="https://docs.h5py.org/en/stable/licenses.html">h5py</a></li>'
            '<li><a href="https://numpy.org/doc/stable/license.html">numpy</a></li>'
            '<li><a href="https://github.com/SethMMorton/natsort">natsort</a></li>'
            '<li><a href="https://github.com/pypa/setuptools">setuptools</a></li>'
            '<li><a href="https://www.pyqtgraph.org/">pyqtgraph</a></li>'
            '<li><a href="https://pyinstaller.org/en/stable/license.html">PyInstaller</a></li>'
            '<li><a href="https://jrsoftware.org/isinfo.php">Inno Setup</a></li>'
            "</ul>"
            "All icons are part of the <i>Core Line - Free</i> Icon-set from "
            '<a href="https://www.streamlinehq.com/">Streamline</a>'
            "and are licensed under a "
            '<a href="https://www.streamlinehq.com/license-freeLinkware">Link-ware License</a>.'
        )
