# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:36:38 2020

@author: Davide Laghi
"""

import MCTAL_READER as mtal
import xlwings as xw
import pandas as pd
import os
import shutil
# import plotter
# from tqdm import tqdm
# import atlas as at
import numpy as np
import string
from outputFile import OutputFile


class BenchmarkOutput:

    def __init__(self, lib, testname, session):
        """
        General class for a Benchmark output

        Parameters
        ----------
        lib : str
            library to post-process
        testname : str
            Name of the benchmark
        session: Session
            Jade Session

        Returns
        -------
        None.

        """
        self.raw_data = {}  # Raw data
        self.testname = testname  # test name
        self.code_path = os.getcwd()  # path to code

        # Read specific configuration
        self.cnf_path = os.path.join(session.path_cnf, testname+'.xlsx')

        # COMPARISON
        if type(lib) == list and len(lib) > 1:
            self.single = False  # Indicator for single or comparison
            self.lib = lib
            couples = []
            tp = os.path.join(session.path_run, lib[0], testname)
            self.test_path = {lib[0]: tp}
            name = lib[0]
            for library in lib[1:]:
                name_couple = lib[0]+'_Vs_'+library
                name = name+'_Vs_'+library
                couples.append((lib[0], library, name_couple))
                tp = os.path.join(session.path_run, library, testname)
                self.test_path[library] = tp

            self.name = name
            # Generate library output path
            out = os.path.join(session.path_comparison, name)
            if not os.path.exists(out):
                os.mkdir(out)

            out = os.path.join(out, testname)
            if os.path.exists(out):
                shutil.rmtree(out)
            os.mkdir(out)
            excel_path = os.path.join(out, 'Excel')
            atlas_path = os.path.join(out, 'Atlas')
            # raw_path = os.path.join(out, 'Raw Data')
            os.mkdir(excel_path)
            os.mkdir(atlas_path)
            # os.mkdir(raw_path)
            self.excel_path = excel_path
            # self.raw_path = raw_path
            self.atlas_path = atlas_path

            self.couples = couples  # Couples of libraries to post process

        # SINGLE-LIBRARY
        else:
            self.single = True  # Indicator for single or comparison
            self.lib = str(lib)  # In case of 1-item list
            self.test_path = os.path.join(session.path_run, lib, testname)

            # Generate library output path
            out = os.path.join(session.path_single, lib)
            if not os.path.exists(out):
                os.mkdir(out)

            out = os.path.join(out, testname)
            if os.path.exists(out):
                shutil.rmtree(out)
            os.mkdir(out)
            excel_path = os.path.join(out, 'Excel')
            atlas_path = os.path.join(out, 'Atlas')
            raw_path = os.path.join(out, 'Raw Data')
            os.mkdir(excel_path)
            os.mkdir(atlas_path)
            os.mkdir(raw_path)
            self.excel_path = excel_path
            self.raw_path = raw_path
            self.atlas_path = atlas_path

    def single_postprocess(self, libmanager):
        """
        Execute the full post-processing of a single library (i.e. excel,
        raw data and atlas)

        Returns
        -------
        None.

        """
        print(' Generating Excel Recap...')
        self._generate_single_excel_output()
        self._print_raw()

        # print(' Creating Atlas...')
        # outpath = os.path.join(self.atlas_path, 'tmp')
        # os.mkdir(outpath)

        # for tally, title, ylabel in \
        #     [(2, 'Leakage Neutron Flux (175 groups)',
        #       'Neutron Flux $[\#/cm^2]$'),
        #      (32, 'Leakage Gamma Flux (24 groups)',
        #       'Gamma Flux $[\#/cm^2]$')]:

        #     print(' Plotting tally n.'+str(tally))
        #     for zaidnum, output in tqdm(self.outputs.items()):
        #         title = title
        #         tally_data = output.mdata.set_index('Tally N.').loc[tally]
        #         energy = tally_data['Energy'].values
        #         values = tally_data['Value'].values
        #         error = tally_data['Error'].values
        #         lib = {'x': energy, 'y': values, 'err': error,
        #                'ylabel': str(zaidnum)+'.'+self.lib}
        #         data = [lib]
        #         outname = str(zaidnum)+'-'+self.lib+'-'+str(tally)
        #         plot = plotter.Plotter(data, title, outpath, outname)
        #         plot.binned_plot(ylabel)

        # print(' Generating Plots Atlas...')
        # # Printing Atlas
        # template = os.path.join(self.code_path, 'Templates',
        #                         'AtlasTemplate.docx')
        # atlas = at.Atlas(template, self.lib)
        # atlas.build(outpath, libmanager)
        # atlas.save(self.atlas_path)
        # # Remove tmp images
        # shutil.rmtree(outpath)

        print(' Single library post-processing completed')

    def compare(self, state, libmanager):
        print(' Generating Excel Recap...')
        self._generate_comparison_excel_output()
        # print(' Creating Atlas...')
        # outpath = os.path.join(self.atlas_path, 'tmp')
        # os.mkdir(outpath)

        # libraries = []
        # outputs = []
        # zaids = []
        # for libname, outputslib in self.outputs.items():
        #     libraries.append(libname)
        #     outputs.append(outputslib)
        #     zaids.append(list(outputslib.keys()))

        # # Extend list to all zaids
        # allzaids = zaids[0]
        # for zaidlist in zaids[1:]:
        #     allzaids.extend(zaidlist)
        # allzaids = set(allzaids)  # no duplicates

        # globalname = ''
        # for lib in libraries:
        #     globalname = globalname + lib + '_Vs_'

        # globalname = globalname[:-4]

        # for tally, title, ylabel in \
        #     [(2, 'Leakage Neutron Flux (175 groups)',
        #       'Neutron Flux $[\#/cm^2]$'),
        #      (32, 'Leakage Gamma Flux (24 groups)',
        #       'Gamma Flux $[\#/cm^2]$')]:

        #     print(' Plotting tally n.'+str(tally))
        #     for zaidnum in tqdm(allzaids):
        #         # title = title
        #         data = []
        #         for idx, output in enumerate(outputs):
        #             try:  # Zaid could not be common to the libraries
        #                 tally_data = output[zaidnum].tallydata.set_index('Tally N.').loc[tally]
        #                 energy = tally_data['Energy'].values
        #                 values = tally_data['Value'].values
        #                 error = tally_data['Error'].values
        #                 lib = {'x': energy, 'y': values, 'err': error,
        #                        'ylabel': str(zaidnum)+'.'+libraries[idx]}
        #                 data.append(lib)
        #             except KeyError:
        #                 # It is ok, simply nothing to plot here
        #                 pass

        #         outname = str(zaidnum)+'-'+globalname+'-'+str(tally)
        #         plot = plotter.Plotter(data, title, outpath, outname)
        #         plot.binned_plot(ylabel)

        # print(' Generating Plots Atlas...')
        # # Printing Atlas
        # template = os.path.join(self.code_path, 'Templates',
        #                         'AtlasTemplate.docx')
        # atlas = at.Atlas(template, globalname)
        # atlas.build(outpath, libmanager)
        # atlas.save(self.atlas_path)
        # # Remove tmp images
        # shutil.rmtree(outpath)

    def _generate_single_excel_output(self):

        # Get excel configuration
        ex_cnf = pd.read_excel(self.cnf_path, sheet_name='Excel')
        ex_cnf.set_index('Tally', inplace=True)

        # Open the excel file
        name = 'Generic_single.xlsx'
        template = os.path.join(os.getcwd(), 'Templates', name)
        outpath = os.path.join(self.excel_path, self.testname + '_' +
                               self.lib+'.xlsx')
        ex = ExcelOutputSheet(template, outpath)
        # Get results
        # results = []
        # errors = []
        results_path = self.test_path

        # Get mfile and outfile
        for file in os.listdir(results_path):
            if file[-1] == 'm':
                mfile = file
            elif file[-1] == 'o':
                ofile = file
        # Parse output
        mcnp_output = MCNPoutput(os.path.join(results_path, mfile),
                                 os.path.join(results_path, ofile))
        mctal = mcnp_output.mctal
        # Adjourn raw Data
        self.raw_data = mcnp_output.tallydata

        # res, err = output.get_single_excel_data()

        for label in ['Value', 'Error']:
            # keys = {}
            for tally in mctal.tallies:
                num = tally.tallyNumber
                key = tally.tallyComment[0]
                # keys[num] = key  # Memorize tally descriptions
                tdata = mcnp_output.tallydata[num].copy()  # Full tally data
                try:
                    tally_settings = ex_cnf.loc[num]
                except KeyError:
                    print(' Warning!: tally n.'+str(num) +
                          ' is not in configuration')
                    continue

                # Re-Elaborate tdata Dataframe
                x_name = tally_settings['x']
                x_tag = tally_settings['x name']
                y_name = tally_settings['y']
                y_tag = tally_settings['y name']
                ylim = tally_settings['cut Y']
                # select the index format
                if x_name == 'Energy':
                    idx_format = '0.00E+00'
                    # TODO all possible cases should be addressed
                else:
                    idx_format = '0'

                if y_name != 'tally':
                    tdata.set_index(x_name, inplace=True)
                    x_set = list(set(tdata.index))
                    y_set = list(set(tdata[y_name].values))
                    rows = []
                    for xval in x_set:
                        row = tdata.loc[xval, label].values
                        rows.append(row)
                    main_value_df = pd.DataFrame(rows, columns=y_set,
                                                 index=x_set)
                    # reorder index
                    main_value_df['index'] = pd.to_numeric(x_set,
                                                           errors='coerce')
                    main_value_df.sort_values('index', inplace=True)
                    del main_value_df['index']
                    # insert the df in pieces
                    ex.insert_cutted_df('B', main_value_df, label+'s', ylim,
                                        header=(key, 'Tally n.'+str(num)),
                                        index_name=x_tag, cols_name=y_tag,
                                        index_num_format=idx_format)
                else:
                    # reorder df
                    tdata['index'] = pd.to_numeric(tdata[x_name],
                                                   errors='coerce')
                    tdata.sort_values('index', inplace=True)
                    del tdata['index']

                    if label == 'Value':
                        del tdata['Error']
                    elif label == 'Error':
                        del tdata['Value']
                    # Insert DF
                    ex.insert_df('B', tdata, label+'s', print_index=False,
                                 header=(key, 'Tally n.'+str(num)))

            # Compile general infos in the sheet
            ws = ex.current_ws
            title = self.testname+' RESULTS RECAP: '+label+'s'
            ws.range('A3').value = title
            ws.range('C1').value = self.lib

        # --- Compile statistical checks sheet ---
        ws = ex.wb.sheets['Statistical Checks']

        dic_checks = mcnp_output.out.stat_checks
        rows = []
        for tally in mctal.tallies:
            num = tally.tallyNumber
            key = tally.tallyComment[0]
            key_dic = key+' ['+str(num)+']'
            try:
                stat = dic_checks[key_dic]
            except KeyError:
                stat = None
            rows.append([num, key, stat])

        df = pd.DataFrame(rows)
        ws.range('A9').options(index=False, header=False).value = df

        ex.save()

    def _print_raw(self):
        for key, data in self.raw_data.items():
            file = os.path.join(self.raw_path, str(key)+'.csv')
            data.to_csv(file, header=True, index=False)

    def _generate_comparison_excel_output(self):

        # Get excel configuration
        ex_cnf = pd.read_excel(self.cnf_path, sheet_name='Excel')
        ex_cnf.set_index('Tally', inplace=True)

        # Open the excel file
        name_tag = 'Generic_comparison.xlsx'
        template = os.path.join(os.getcwd(), 'Templates', name_tag)

        mcnp_outputs = {}
        iteration = 0
        for reflib, tarlib, name in self.couples:
            iteration = iteration+1
            outpath = os.path.join(self.excel_path, self.name+'_Comparison_' +
                                   name+'.xlsx')
            ex = ExcelOutputSheet(template, outpath)
            # Get results
            if iteration == 1:
                to_read = [reflib, tarlib]
            else:
                to_read = [tarlib]

            for lib in to_read:
                results_path = self.test_path[lib]

                # Get mfile and outfile
                for file in os.listdir(results_path):
                    if file[-1] == 'm':
                        mfile = file
                    elif file[-1] == 'o':
                        ofile = file
                # Parse output
                mcnp_output = MCNPoutput(os.path.join(results_path, mfile),
                                         os.path.join(results_path, ofile))
                mcnp_outputs[lib] = mcnp_output

            # Build the comparison
            for tally in mcnp_outputs[reflib].mctal.tallies:
                num = tally.tallyNumber
                key = tally.tallyComment[0]

                # Full tally data
                tdata_ref = mcnp_outputs[reflib].tallydata[num].copy()
                tdata_tar = mcnp_outputs[tarlib].tallydata[num].copy()
                try:
                    tally_settings = ex_cnf.loc[num]
                except KeyError:
                    print(' Warning!: tally n.'+str(num) +
                          ' is not in configuration')
                    continue

                # Re-Elaborate tdata Dataframe
                x_name = tally_settings['x']
                x_tag = tally_settings['x name']
                y_name = tally_settings['y']
                y_tag = tally_settings['y name']
                ylim = tally_settings['cut Y']
                # select the index format
                if x_name == 'Energy':
                    idx_format = '0.00E+00'
                    # TODO all possible cases should be addressed
                else:
                    idx_format = '0'

                if y_name != 'tally':
                    tdata_ref.set_index(x_name, inplace=True)
                    tdata_tar.set_index(x_name, inplace=True)
                    x_set = list(set(tdata_ref.index))
                    y_set = list(set(tdata_ref[y_name].values))
                    rows = []
                    for xval in x_set:
                        # !!! True divide warnings are suppressed !!!
                        with np.errstate(divide='ignore', invalid='ignore'):
                            row = ((tdata_ref.loc[xval, 'Value'].values -
                                   tdata_tar.loc[xval, 'Value'].values) /
                                   tdata_ref.loc[xval, 'Value'].values)
                        rows.append(row)
                    main_value_df = pd.DataFrame(rows, columns=y_set,
                                                 index=x_set)
                    # reorder index
                    main_value_df['index'] = pd.to_numeric(x_set,
                                                           errors='coerce')
                    main_value_df.sort_values('index', inplace=True)
                    del main_value_df['index']
                    # insert the df in pieces
                    ex.insert_cutted_df('B', main_value_df, 'Comparison', ylim,
                                        header=(key, 'Tally n.'+str(num)),
                                        index_name=x_tag, cols_name=y_tag,
                                        index_num_format=idx_format)
                else:
                    # reorder df
                    for tdata in [tdata_ref, tdata_tar]:
                        tdata['index'] = pd.to_numeric(tdata[x_name],
                                                       errors='coerce')
                        tdata.sort_values('index', inplace=True)
                        del tdata['index']
                        del tdata['Error']
                    
                    # !!! True divide warnings are suppressed !!!
                    with np.errstate(divide='ignore', invalid='ignore'):
                        df = (tdata_ref-tdata_tar)/tdata_ref

                    # Insert DF
                    ex.insert_df('B', df, 'Comparison', print_index=False,
                                 header=(key, 'Tally n.'+str(num)))

            # Compile general infos in the sheet
            ws = ex.current_ws
            title = self.testname+' RESULTS RECAP: Comparison'
            ws.range('A3').value = title
            ws.range('C1').value = tarlib+' Vs '+reflib

            ex.save()


class MCNPoutput:
    def __init__(self, mctal_file, output_file):
        """
        Class handling an MCNP run Output

        mctal_file: (str/path) path to the mctal file
        """
        self.mctal_file = mctal_file  # path to mctal file
        self.output_file = output_file  # path to mcnp output file

        # Read and parse the mctal file
        mctal = mtal.MCTAL(mctal_file)
        mctal.Read()
        self.mctal = mctal
        self.tallydata, self.totalbin = self.organize_mctal()

        # Read the output file
        self.out = OutputFile(output_file)
        self.out.assign_tally_description(self.mctal.tallies)
        self.stat_checks = self.out.stat_checks

    def organize_mctal(self):
        """
        Retrieve and organize mctal data into a DataFrame.

        Returns: DataFrame containing the organized data
        """
        tallydata = {}
        totalbin = {}

        for t in self.mctal.tallies:
            rows = []

            # --- Reorganize values ---
            nDir = t.getNbins("d", False)
            nMul = t.getNbins("m", False)
            # Some checks for voids
            binnings = {'cells': t.cells, 'user': t.usr, 'segments': t.seg,
                        'cosine': t.cos, 'energy': t.erg, 'time': t.tim,
                        'cor A': t.cora, 'cor B': t.corb, 'cor C': t.corc}

            for name, binning in binnings.items():
                if len(binning) == 0:
                    binnings[name] = [np.nan]
            # Start iteration
            for f, fn in enumerate(binnings['cells']):
                for d in range(nDir):  # Unused
                    for u, un in enumerate(binnings['user']):
                        for s, sn in enumerate(binnings['segments']):
                            for m in range(nMul):  # (unused)
                                for c, cn in enumerate(binnings['cosine']):
                                    for e, en in enumerate(binnings['energy']):
                                        for nt, ntn in enumerate(binnings['time']):
                                            for k, kn in enumerate(binnings['cor C']):
                                                for j, jn in enumerate(binnings['cor B']):
                                                    for i, ina in enumerate(binnings['cor A']):
                                                        val = t.getValue(f, d, u, s, m, c, e, nt, i, j, k, 0)
                                                        err = t.getValue(f, d, u, s, m, c, e, nt, i, j, k, 1)
                                                        rows.append([fn, d, un, sn, m, cn, en, ntn, ina, jn, kn, val,err])

                # Only one total bin per cell is admitted
                val = t.getValue(f, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0)
                err = t.getValue(f, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1)
                if t.timTC is not None:
                    rows.append([fn, d, un, sn, m, cn, en, 'total', ina, jn,
                                 kn, val, err])
                    total = 'Time'
                elif t.ergTC is not None:
                    rows.append([fn, d, un, sn, m, cn, 'total', ntn, ina, jn,
                                 kn, val, err])
                    total = 'Energy'
                elif t.cosTC is not None:
                    rows.append([fn, d, un, sn, m, 'total', en, ntn, ina, jn,
                                 kn, val, err])
                    total = 'Cosine'

            # --- Build the tally DataFrame ---
            columns = ['Cells', 'Dir', 'User', 'Segments',
                       'Multiplier', 'Cosine', 'Energy', 'Time',
                       'Cor C', 'Cor B', 'Cor A', 'Value', 'Error']
            df = pd.DataFrame(rows, columns=columns)

            # Default drop of multiplier and Dir
            del df['Dir']
            del df['Multiplier']
            df.dropna(axis=1, inplace=True)  # Keep only meaningful binning

            # Sub DF containing only total bins
            try:
                dftotal = df[df[total] == 'total']
            except KeyError:
                dftotal = None

            tallydata[t.tallyNumber] = df
            totalbin[t.tallyNumber] = dftotal

        return tallydata, totalbin


class ExcelOutputSheet:
    # Common variables
    _starting_free_row = 10

    def __init__(self, template, outpath):
        """
        Excel sheet reporting the outcome of an MCNP test

        template: (str/path) path to the sheet template
        """
        self.outpath = outpath  # Path to the excel file
        # Open template
        shutil.copy(template, outpath)
        self.app = xw.App(visible=False)
        self.wb = self.app.books.open(outpath)
        # The first open row in current ws
        self.free_row = self._starting_free_row
        self.ws_free_rows = {}
        self.current_ws = None

    def _switch_ws(self, ws_name):
        """
        Change active worksheet without loosing parameters informations.

        Parameters
        ----------
        ws_name : str
            Worksheet name.

        Returns
        -------
        ws : xlwings.Sheet
            Excel worksheet.

        """
        # Adjourn free row sheet
        if self.current_ws is not None:
            self.ws_free_rows[self.current_ws.name] = self.free_row

        # Select new sheet
        ws = self.wb.sheets[ws_name]
        self.current_ws = ws
        try:
            self.free_row = self.ws_free_rows[ws_name]
        except KeyError:
            self.free_row = self._starting_free_row

        return ws

    def insert_df(self, startcolumn, df, ws, startrow=None, header=None,
                  print_index=True, idx_format='0', cols_head_size=12):
        '''
        Insert a DataFrame (df) into a Worksheet (ws) using xlwings.

        Parameters
        ----------
        startcolumn : int or str
            Starting column where to insert the DataFrame. It can be expressed
            both as an integer as a letter in Excel fashion.
        df : pandas.DataFrame
            DataFrame to insert in the excel sheet
        ws : str
            name of the Excel worksheet where to put the DataFrame.
        startrow : int
            starting row where to put the DataFrame. Default is None that
            triggers the use of the memorized first free row in the excel sheet
        header : tuple (str, value)
            contains the tag of the header and the header value. DEAFAULT is
            None
        print_index : bool
            if True the DataFrame index is printed. DEAFAULT is True.
        idx_format : str
            how to format the index values. DEAFAULT is '0' (integer)
        cols_head_size : int
            Font size for columns header. DEAFAULT is 12

        Returns
        -------
        None

        '''
        if startrow is None:
            startrow = self.free_row
            # adjourn free row
            add_space = 3  # Includes header
            self.free_row = self.free_row + len(df) + add_space

        ws = self._switch_ws(ws)
        # ws = self.wb.sheets[ws]
        # Start column can be provided as a letter or number (up to Z)
        if type(startcolumn) is str:
            startcolumn = ord(startcolumn.lower())-96

        anchor = (startrow, startcolumn)
        header_anchor_tag = (startrow, 1)
        header_anchor = (startrow+1, 1)

        try:
            ws.range(anchor).options(index=print_index, header=True).value = df
            rng = ((startrow+1, startcolumn),
                   (startrow+1+len(df), startcolumn))

            # Formatting
            ws.range(*rng).number_format = idx_format  # idx formatting
            # Columns headers
            anchor_columns = (anchor, (startrow, startcolumn+len(df.columns)))
            ws.range(*anchor_columns).api.Font.Size = cols_head_size
            ws.range(*anchor_columns).api.Font.Bold = True
            ws.range(*anchor_columns).color = (236, 236, 236)

            if header is not None:
                ws.range(header_anchor_tag).value = header[0]
                ws.range(header_anchor_tag).api.Font.Size = cols_head_size
                ws.range(header_anchor_tag).api.Font.Bold = True
                ws.range(header_anchor_tag).color = (236, 236, 236)

                ws.range(header_anchor).value = header[1]
                ws.range(header_anchor).api.Font.Size = cols_head_size
                ws.range(header_anchor_tag).api.Font.Bold = True
                ws.range(header_anchor_tag).color = (236, 236, 236)

        except Exception as e:
            print(vars(e))
            print(header)
            print(df)

    def insert_cutted_df(self, startcolumn, df, ws, ylim, startrow=None,
                         header=None, index_name=None, cols_name=None,
                         index_num_format='0'):
        """
        Insert a DataFrame in the excel cutting its columns

        Parameters
        ----------
        startcolumn : str/int
            Excel column where to put the first DF column.
        df : pd.DataFrame
            global DF to insert.
        ws : str
            Excel worksheet where to insert the DF.
        ylim : int
            limit of columns to use to cut the DF.
        startrow : int, optional
            initial Excel row. The default is None,
            the first available is used.
        header : tuple (str, value)
            contains the tag of the header and the header value. DEAFAULT is
            None
        index_name : str
            Name of the Index. DEAFAULT is None
        cols_name : str
            Name of the columns. DEFAULT is None
        index_num_format: str
            format of index numbers

        Returns
        -------
        None.

        """
        res_len = len(df.columns)
        start_col = 0
        ylim = int(ylim)
        # ws = self.wb.sheets[ws]
        # Decode columns for index and columns names
        if type(startcolumn) is int:
            index_col = string.ascii_uppercase[startcolumn]
            columns_col = string.ascii_uppercase[startcolumn+1]
        elif type(startcolumn) is str:
            index_col = startcolumn
            columns_col = chr(ord(startcolumn)+1)

        # Add each DataFrame piece
        new_ylim = ylim
        while res_len > ylim:
            curr_df = df.iloc[:, start_col:new_ylim]
            # Memorize anchors for headers name
            anchor_index = index_col+str(self.free_row)
            anchor_cols = columns_col+str(self.free_row-1)
            end_anchor_cols = (chr(ord(columns_col)+len(curr_df.columns)-1) +
                               str(self.free_row-1))
            # Insert cutted df
            self.insert_df(startcolumn, curr_df, ws, header=header,
                           idx_format=index_num_format)
            # Insert columns name and index name
            self.current_ws.range(anchor_index).value = index_name
            self.current_ws.range(anchor_index).api.Font.Size = 12
            self.current_ws.range(anchor_index).api.Font.Bold = True
            self.current_ws.range(anchor_index).color = (236, 236, 236)

            self.current_ws.range(anchor_cols).value = cols_name
            self.current_ws.range(anchor_cols).api.Font.Size = 12
            self.current_ws.range(anchor_cols).api.Font.Bold = True
            self.current_ws.range(anchor_cols).color = (236, 236, 236)
            self.current_ws.range(anchor_cols+':'+end_anchor_cols).merge()
            # Adjourn parameters
            start_col = start_col+ylim
            new_ylim = new_ylim+ylim
            res_len = res_len-ylim

        # Add the remaining piece
        if res_len != 0:
            curr_df = df.iloc[:, -res_len:]
            # Memorize anchors for headers name
            anchor_index = index_col+str(self.free_row)
            anchor_cols = columns_col+str(self.free_row-1)
            end_anchor_cols = (chr(ord(columns_col)+len(curr_df.columns)-1) +
                               str(self.free_row-1))

            self.insert_df(startcolumn, curr_df, ws, header=header,
                           idx_format=index_num_format)
            # Insert columns name and index name
            self.current_ws.range(anchor_index).value = index_name
            self.current_ws.range(anchor_cols).value = cols_name
            # Merge the cols name
            self.current_ws.range(anchor_cols+':'+end_anchor_cols).merge()

        # Adjust lenght
        self.current_ws.range(index_col+':AAA').autofit()

    def copy_sheets(self, wb_origin_path):
        """
        Copy all sheets of the selected excel file into the current one

        Parameters
        ----------
        wb_origin_path : str/path
            Path to excel file containing sheets to add.

        Returns
        -------
        None.

        """
        wb = self.app.books.open(wb_origin_path)
        for sheet in wb.sheets:

            # copy to a new workbook
            sheet.api.Copy()

            # copy to an existing workbook by putting it in front of a
            # worksheet object
            sheet.api.Copy(Before=self.wb.sheets[0].api)

    def save(self):
        """
        Save Excel
        """
        self.app.calculate()
        self.wb.save()
        self.wb.close()
        self.app.quit()
