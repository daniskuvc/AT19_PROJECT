#
# @results_data.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


class Results:
    """Contains the results data"""
    def __init__(self, results, word, model):
        """Defines the constructor"""
        self.ml_results = results
        for item in self.ml_results:
            item['word'] = word
            item['model'] = model

    def results(self):
        """Returns the list with the results"""
        return self.ml_results