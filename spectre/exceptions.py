# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later


class ChunkExistsError(FileExistsError): ...

class ChunkNotFoundError(FileNotFoundError): ...
class ChunkFileNotFoundError(FileNotFoundError): ...
class SpectrogramNotFoundError(FileNotFoundError): ...
class LogNotFoundError(FileNotFoundError): ...
class CaptureConfigNotFoundError(FileNotFoundError): ...
class FitsConfigNotFoundError(FileNotFoundError): ...

class ReceiverNotFoundError(KeyError): ...
class ModeNotFoundError(KeyError): ...
class SpecificationNotFoundError(KeyError): ...
class TagNotFoundError(ValueError): ...
class PanelNotFoundError(KeyError): ...
class EventHandlerNotFoundError(KeyError): ...
class TemplateNotFoundError(KeyError): ...
class InvalidSpecificationError(KeyError): ...
class InvalidReceiverError(KeyError): ...
class InvalidModeError(KeyError): ...

class InvalidMetadataError(ValueError): ...
class InvalidTagError(ValueError): ...
class InvalidSweepMetadataError(InvalidMetadataError): ...

