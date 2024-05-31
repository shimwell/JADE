# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:53:52 2021

@author: Davide Laghi

Copyright 2021, the JADE Development Team. All rights reserved.

This file is part of JADE.

JADE is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

JADE is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with JADE.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys
import os
import json

cp = os.path.dirname(os.path.abspath(__file__))
modules_path = os.path.dirname(cp)
sys.path.insert(1, modules_path)

from jade.libmanager import LibManager
from jade.configuration import Configuration
import jade.output as output
from jade.expoutput import SpectrumOutput
from jade.sphereoutput import SphereOutput
from jade.configuration import Configuration
from jade.__version__ import __version__


# Files
OUTP_SDDR = os.path.join(
    cp, "TestFiles", "sphereoutput", "SphereSDDR_11023_Na-23_102_o"
)
OUTM_SDDR = os.path.join(
    cp, "TestFiles", "sphereoutput", "SphereSDDR_11023_Na-23_102_m"
)


class MockSession:
    def __init__(self, conf: Configuration, root_dir: os.PathLike) -> None:
        self.state = "dummy"
        self.path_templates = os.path.join(modules_path, "jade", "templates")
        self.path_cnf = os.path.join(
            modules_path,
            "jade",
            "default_settings",
            "Benchmarks_Configuration",
        )
        self.path_run = os.path.join(cp, "TestFiles", "output", "Simulations")
        self.conf = conf
        self.path_comparison = root_dir.mkdir("comparison")
        self.path_single = root_dir.mkdir("single")
        self.path_exp_res = os.path.join(
            modules_path, "jade", "install_files", "Experimental_Results"
        )


class TestSphereSDDRMCNPoutput:

    def test_organizemctal(self):
        out = output.MCNPoutput(OUTM_SDDR, OUTP_SDDR)
        t4 = out.tallydata[4]
        t2 = out.tallydata[2]
        assert list(t4.columns) == ["Cells", "Segments", "Value", "Error"]
        assert len(t4) == 1
        assert len(t2) == 176
        assert list(t2.columns) == ["Energy", "Value", "Error"]


class TestBenchmarkOutput:

    def test_single_excel(self, tmpdir):
        conf = Configuration(
            os.path.join(cp, "TestFiles", "output", "config_test.xlsx")
        )
        session = MockSession(conf, tmpdir)
        out = output.BenchmarkOutput("32c", "mcnp", "ITER_1D", session)
        out._generate_single_excel_output()
        out._print_raw()

        assert os.path.exists(
            os.path.join(
                session.path_single, r"32c\ITER_1D\mcnp\Excel\ITER_1D_32c.xlsx"
            )
        )
        metadata_path = os.path.join(
            session.path_single, r"32c\ITER_1D\mcnp\Raw_Data\metadata.json"
        )
        assert os.path.exists(metadata_path)
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
        assert metadata["jade_run_version"] == "0.0.1"
        assert metadata["jade_version"] == __version__


class TestExperimentalOutput:

    def test_print_raw_metadata(self, tmpdir):
        conf = Configuration(
            os.path.join(cp, "TestFiles", "output", "config_test.xlsx")
        )
        session = MockSession(conf, tmpdir)
        out = SpectrumOutput(
            ["Exp", "32c"], "mcnp", "Oktavian", session, multiplerun=True
        )
        out._extract_outputs()
        out._read_exp_results()
        out._print_raw()

        for folder in os.listdir(session.path_comparison):
            path = os.path.join(
                session.path_comparison,
                folder,
                "Oktavian",
                "mcnp",
                "Raw_Data",
                "32c",
                "metadata.json",
            )

            assert os.path.exists(path)
            with open(path, "r") as f:
                metadata = json.load(f)
            assert metadata["jade_run_version"] == "0.0.1"
            assert metadata["jade_version"] == __version__
