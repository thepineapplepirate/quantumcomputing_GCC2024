# (C) Copyright IBM 2021, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""An interface for sampling problems."""
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from qiskit_algorithms import MinimumEigensolverResult

# from qiskit.opflow import PauliOp, PauliSumOp
from qiskit.quantum_info import SparsePauliOp

if TYPE_CHECKING:
    from .protein_folding_result import ProteinFoldingResult


class SamplingProblem(ABC):
    """An interface for sampling problems."""

    @abstractmethod
    def qubit_op(self) -> SparsePauliOp:
        """Returns a qubit operator that represents a Hamiltonian encoding the sampling problem."""

    @abstractmethod
    def interpret(self, raw_result: MinimumEigensolverResult) -> "ProteinFoldingResult":
        """Interprets results of an optimization."""
