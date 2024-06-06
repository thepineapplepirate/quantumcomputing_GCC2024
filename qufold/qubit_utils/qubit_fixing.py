# (C) Copyright IBM 2021, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""Changes certain qubits to fixed values."""
from typing import Union

import numpy as np

# from qiskit.opflow import PauliSumOp, OperatorBase, PauliOp
from qiskit.quantum_info import PauliList, SparsePauliOp


def _fix_qubits(
    operator: Union[int, SparsePauliOp],
    has_side_chain_second_bead: bool = False,
) -> Union[int, SparsePauliOp]:
    """
    Assigns predefined values for turns qubits on positions 0, 1, 2, 3, 5 in the main chain without the loss of generality (see the paper https://arxiv.org/pdf/1908.02163.pdf). Qubits on these position are considered fixed and not subject to optimization.

    Args:
        operator: an operator whose qubits shall be fixed.

    Returns:
        An operator with relevant qubits changed to fixed values.
    """
    # operator might be 0 (int) because it is initialized as operator = 0; then we should not attempt fixing qubits
    if not isinstance(operator, SparsePauliOp):
        return operator
    operator = operator.simplify()
    new_tables_x = []
    new_tables_z = []
    new_coeffs = []

    for hamiltonian in operator:
        table_z = np.copy(hamiltonian.paulis.z[0])
        table_x = np.copy(hamiltonian.paulis.x[0])
        coeffs = _calc_updated_coeffs(hamiltonian, table_z, has_side_chain_second_bead)
        _preset_binary_vals(table_z, has_side_chain_second_bead)
        new_tables_x.append(table_x)
        new_tables_z.append(table_z)
        new_coeffs.append(coeffs)
    new_pauli_table = PauliList.from_symplectic(new_tables_z, new_tables_x)
    operator_updated = SparsePauliOp(data=new_pauli_table, coeffs=new_coeffs)
    operator_updated = operator_updated.simplify()
    return operator_updated


def _calc_updated_coeffs(
    hamiltonian: SparsePauliOp, table_z, has_side_chain_second_bead: bool
) -> np.ndarray:
    coeffs = np.copy(hamiltonian.coeffs[0])
    if len(table_z) > 1 and table_z[1] == np.bool_(True):
        coeffs = -1 * coeffs
    if (
        not has_side_chain_second_bead
        and len(table_z) > 6
        and table_z[5] == np.bool_(True)
    ):
        coeffs = -1 * coeffs
    return coeffs


def _preset_binary_vals(table_z, has_side_chain_second_bead: bool):
    main_beads_indices = [0, 1, 2, 3]
    if not has_side_chain_second_bead:
        main_beads_indices.append(5)
    for index in main_beads_indices:
        _preset_single_binary_val(table_z, index)


def _preset_single_binary_val(table_z, index: int):
    try:
        table_z[index] = np.bool_(False)
    except IndexError:
        pass
