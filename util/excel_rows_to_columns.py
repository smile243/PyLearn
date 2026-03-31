#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
读取一个 Excel 文件:
- Sheet 1: 取行号为 3 的倍数的行, 合并成一列, 写入 Sheet 3 (Transformed).
- Sheet 1: 从第 2 行开始每隔 3 行取一次 (2,5,8,...), 写入 Transformed_goal.
- Sheet 2: 第 1、2 列中的每个值按 (sheet1 的有效列数) 重复, 写入第 4、5 列;
  第 3 列按整体列块的方式按 (sheet2 第 1 列的有效行数) 重复, 写入第 6 列.
"""

import argparse
import os
from typing import List, Any

from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet


def parseArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sheet 1 merged result -> sheet 3; replicate sheet 2 cols 1-3 by effective col count to cols 4-6."
    )
    parser.add_argument(
        "-i", "--input",
        default="test.xlsx",
        help="Input Excel file path (default: test.xlsx)"
    )
    parser.add_argument(
        "-o", "--output-sheet",
        default="Transformed",
        help="Name of the new sheet for sheet-1 result (default: Transformed, written as 3rd sheet)"
    )
    parser.add_argument(
        "-o-file", "--output-file",
        default=None,
        help="Output Excel file path (default: overwrite input file)"
    )
    return parser.parse_args()


def getRowsAtMultipleOfN(ws: Worksheet, n: int) -> List[List[Any]]:
    """
    获取 1-based 行号为 n 倍数的所有行.
    返回一个行列表, 其中每一行都是单元格值组成的列表.
    """
    rows: List[List[Any]] = []
    for oneBasedRowNum in range(n, ws.max_row + 1, n):
        rowValues = [
            ws.cell(row=oneBasedRowNum, column=col).value
            for col in range(1, ws.max_column + 1)
        ]
        rows.append(rowValues)
    return rows


def getRowsByStartAndStep(ws: Worksheet, startRow: int, step: int) -> List[List[Any]]:
    """
    按 1-based 起始行和步长获取多行.
    例如: startRow=2, step=3 -> 2,5,8,...
    """
    rows: List[List[Any]] = []
    if startRow <= 0 or step <= 0:
        return rows
    for oneBasedRowNum in range(startRow, ws.max_row + 1, step):
        rowValues = [
            ws.cell(row=oneBasedRowNum, column=col).value
            for col in range(1, ws.max_column + 1)
        ]
        rows.append(rowValues)
    return rows


def getEffectiveColumnCount(rows: List[List[Any]]) -> int:
    """
    有效列数: 这些行中最右侧存在任意非空值的列索引.
    """
    if not rows:
        return 0
    for c in range(len(rows[0]) - 1, -1, -1):
        if any(_non_empty(r[c]) for r in rows):
            return c + 1
    return 0


def _non_empty(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, str):
        # Treat whitespace-only cells as empty.
        return v.strip() != ""
    return True


def removeAllSpaces(value: Any) -> Any:
    """
    Remove all whitespace characters from a string.
    Only intended for Sheet2 col3 -> col6 conversion.
    """
    if isinstance(value, str):
        return "".join(value.split())
    return value


def replicateByCount(values: List[Any], count: int) -> List[Any]:
    """
    按顺序将每个值重复 `count` 次.
    例如: values=[A,B], count=3 -> [A,A,A,B,B,B]
    """
    result: List[Any] = []
    for v in values:
        result.extend([v] * count)
    return result


def replicateBlock(block: List[Any], times: int) -> List[Any]:
    """
    将整个列表作为一个整体重复 `times` 次.
    例如: block=[1,2,3,4], times=2 -> [1,2,3,4,1,2,3,4]
    """
    return block * times


def countEffectiveValues(values: List[Any]) -> int:
    """统计列表中的非空值数量 (用于 sheet2 第 1 列的有效行数)."""
    return sum(1 for v in values if _non_empty(v))


def rowsToSingleColumn(rows: List[List[Any]]) -> List[Any]:
    """
    将每一行按纵向展开, 再把所有内容合并成一个单列列表.
    结果示例: [row1_val1, row1_val2, ..., row2_val1, row2_val2, ..., ...]
    """
    if not rows:
        return []
    result: List[Any] = []
    for row in rows:
        result.extend(row)
    return result


def readColumn(ws: Worksheet, col: int) -> List[Any]:
    """读取某一列中的所有值 (1-based)."""
    return [ws.cell(row=r, column=col).value for r in range(1, ws.max_row + 1)]


def main() -> None:
    args = parseArgs()
    inputPath = os.path.abspath(args.input)

    if not os.path.isfile(inputPath):
        print(f"Error: file not found: {inputPath}")
        return

    wb = load_workbook(inputPath, read_only=False)
    ws1 = wb.worksheets[0]

    rows = getRowsAtMultipleOfN(ws1, 3)
    if not rows:
        print("No rows at 3-multiple indices found in the first sheet.")
        return

    effectiveColCount = getEffectiveColumnCount(rows)
    if effectiveColCount <= 0:
        print("Error: effective column count is 0.")
        return

    singleColumn = rowsToSingleColumn(rows)
    goalRows = getRowsByStartAndStep(ws1, startRow=2, step=3)
    goalSingleColumn = rowsToSingleColumn(goalRows)

    # Sheet 2: 第 1、2 列中的每个值按 effectiveColCount 重复后写入第 4、5 列;
    # 第 3 列作为整体按第 1 列的有效行数重复后写入第 6 列
    if len(wb.worksheets) < 2:
        wb.create_sheet(title="Sheet2")
    ws2 = wb.worksheets[1]
    col1Values = readColumn(ws2, 1)
    col2Values = readColumn(ws2, 2)
    col3Values = [removeAllSpaces(v) for v in readColumn(ws2, 3)]
    effectiveRowCount = countEffectiveValues(col1Values)
    if effectiveRowCount <= 0:
        effectiveRowCount = 1
    for srcCol, dstCol, values in [(1, 4, col1Values), (2, 5, col2Values)]:
        replicated = replicateByCount(values, effectiveColCount)
        for r, value in enumerate(replicated, start=1):
            ws2.cell(row=r, column=dstCol, value=value)
    # 第 3 列 -> 第 6 列: 整列作为一个块, 按第 1 列有效行数重复
    # Filter out empty cells first so col6 is compact (no alternating empty rows).
    col3Block = [v for v in col3Values if _non_empty(v)]
    col3Replicated = replicateBlock(col3Block, effectiveRowCount)
    for r, value in enumerate(col3Replicated, start=1):
        ws2.cell(row=r, column=6, value=value)

    # Sheet 3: sheet 1 的合并结果 (3 的倍数行 -> 单列)
    if args.output_sheet in wb.sheetnames:
        del wb[args.output_sheet]
    sheet3 = wb.create_sheet(title=args.output_sheet)
    for r, value in enumerate(singleColumn, start=1):
        sheet3.cell(row=r, column=1, value=value)

    # Transformed_goal: sheet 1 的合并结果 (第 2、5、8... 行 -> 单列)
    goalSheetName = "Transformed_goal"
    if goalSheetName in wb.sheetnames:
        del wb[goalSheetName]
    goalSheet = wb.create_sheet(title=goalSheetName)
    for r, value in enumerate(goalSingleColumn, start=1):
        goalSheet.cell(row=r, column=1, value=value)

    outPath = args.output_file or inputPath
    wb.save(outPath)
    print(
        f"Done. Effective column count: {effectiveColCount}. "
        f"Sheet 2 cols 4-6 filled; sheet '{args.output_sheet}' filled; sheet '{goalSheetName}' filled. "
        f"Saved to {outPath}"
    )


if __name__ == "__main__":
    main()
