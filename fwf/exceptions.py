"""
Copyright 2024 VoxLight

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   /fwf/exceptions.py
"""
class InvalidColumnSpec(Exception): ...
"""
An exception to raise when an invalid ColumnSpec is provided.
"""

class InvalidColumnData(Exception): ...
"""
An exception to raise when an invalid ColumnData is provided.
"""

class InvalidDataRow(Exception): ...
"""
An exception to raise when an invalid RowData is provided.
"""