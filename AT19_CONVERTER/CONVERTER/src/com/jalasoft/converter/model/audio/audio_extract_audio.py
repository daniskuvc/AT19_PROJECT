#
# @audio_extract_audio.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from CONVERTER.src.com.jalasoft.converter.model.converter import Converter
from CONVERTER.src.com.jalasoft.converter.common.exception.converter_exception import ConverterException
from CONVERTER.src.com.jalasoft.converter.common.valid_data import Validations


class ExtractAudio(Converter):
    """Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self) -> str:
        """Creates a command to extracts the audio from a video"""
        Validations().validate_directory(self.input_file, 'vidToaud-')
        Validations().validate_input(self.input_file, 'vidToaud-')
        Validations().validate_output(self.output_file, 'vidToaud-')
        Validations().validate_directory(self.output_file, 'vidToaud-')
        try:
            cmd = f'ffmpeg -i {self.input_file} -vn {self.output_file}'
            return cmd
        except Exception as error:
            raise ConverterException('Create Audio Convert command error')

