# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

class ChunkNotFoundError(FileNotFoundError): ...
class ChunkFileNotFoundError(FileNotFoundError): ...
class SpectrogramNotFoundError(FileNotFoundError): ...
class ModeNotFoundError(KeyError): ...
class EventHandlerNotFoundError(KeyError): ...
class ReceiverNotFoundError(KeyError): ...
class TemplateNotFoundError(KeyError): ...
class SpecificationNotFoundError(KeyError): ...
class PanelNotFoundError(KeyError): ...

class InvalidTagError(ValueError): ...
class InvalidModeError(KeyError): ...
class InvalidSweepMetadataError(ValueError): ...
