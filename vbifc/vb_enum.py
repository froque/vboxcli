# This file is part of vboxcli
# Copyright (C) 2016  Michael Hansen
#
# vboxcli is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# vboxcli is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with vboxcli; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from . import VBoxWrapper

_ac_text_cache = None
def AudioControllerType_text(id):
    global _ac_text_cache
    if _ac_text_cache is None:
        vbox = VBoxWrapper()
        _ac_text_cache = {
            vbox.constants.AudioControllerType_AC97: u'ICH AC97',
            vbox.constants.AudioControllerType_SB16: u'SoundBlaster 16',
            vbox.constants.AudioControllerType_HDA: u'Intel HD Audio'
        }
    if id in _ac_text_cache:
        return _ac_text_cache[id]
    else:
        return u'(Unknown)'

_ad_text_cache = None
def AudioDriverType_text(id):
    global _ad_text_cache
    if _ad_text_cache is None:
        vbox = VBoxWrapper()
        _ad_text_cache = {
            vbox.constants.AudioDriverType_Null: u'Dummy',
            vbox.constants.AudioDriverType_WinMM: u'Windows Multimedia',
            vbox.constants.AudioDriverType_OSS: u'OSS',
            vbox.constants.AudioDriverType_ALSA: u'ALSA',
            vbox.constants.AudioDriverType_DirectSound: u'DirectSound',
            vbox.constants.AudioDriverType_CoreAudio: u'CoreAudio',
            vbox.constants.AudioDriverType_Pulse: u'PulseAudio',
            vbox.constants.AudioDriverType_SolAudio: u'Solaris Audio'
        }
    if id in _ad_text_cache:
        return _ad_text_cache[id]
    else:
        return u'(Unknown)'

_dt_text_cache = None
def DeviceType_text(id):
    global _dt_text_cache
    if _dt_text_cache is None:
        vbox = VBoxWrapper()
        _dt_text_cache = {
            vbox.constants.DeviceType_Null: u'',
            vbox.constants.DeviceType_Floppy: u'Floppy',
            vbox.constants.DeviceType_DVD: u'Optical',
            vbox.constants.DeviceType_HardDisk: u'Hard Disk',
            vbox.constants.DeviceType_Network: u'Network',
            vbox.constants.DeviceType_USB: u'USB',
            vbox.constants.DeviceType_SharedFolder: u'Shared Folder',
            vbox.constants.DeviceType_Graphics3D: u'3D Graphics'
        }
    if id in _dt_text_cache:
        return _dt_text_cache[id]
    else:
        return u'(Unknown)'

_ms_text_cache = None
def MachineState_text(id):
    global _ms_text_cache
    if _ms_text_cache is None:
        vbox = VBoxWrapper()
        _ms_text_cache = {
            vbox.constants.MachineState_Null: u'<Invalid>',
            vbox.constants.MachineState_PoweredOff: u'Powered Off',
            vbox.constants.MachineState_Saved: u'Saved',
            vbox.constants.MachineState_Teleported: u'Teleported',
            vbox.constants.MachineState_Aborted: u'Aborted',
            vbox.constants.MachineState_Running: u'Running',
            vbox.constants.MachineState_Paused: u'Paused',
            vbox.constants.MachineState_Stuck: u'Guru Meditation',
            vbox.constants.MachineState_Teleporting: u'Teleporting',
            vbox.constants.MachineState_LiveSnapshotting: u'Creating Snapshot (Online)',
            vbox.constants.MachineState_Starting: u'Starting',
            vbox.constants.MachineState_Stopping: u'Stopping',
            vbox.constants.MachineState_Saving: u'Saving',
            vbox.constants.MachineState_Restoring: u'Restoring',
            vbox.constants.MachineState_TeleportingPausedVM: u'Teleporting (Paused)',
            vbox.constants.MachineState_TeleportingIn: u'Teleporting In',
            vbox.constants.MachineState_FaultTolerantSyncing: u'Syncing',
            vbox.constants.MachineState_DeletingSnapshotOnline: u'Deleting Snapshot (Online)',
            vbox.constants.MachineState_DeletingSnapshotPaused: u'Deleting Snapshot (Paused)',
            vbox.constants.MachineState_OnlineSnapshotting: u'Creating Snapshot (Online)',
            vbox.constants.MachineState_RestoringSnapshot: u'Restoring Snapshot',
            vbox.constants.MachineState_DeletingSnapshot: u'Deleting Snapshot',
            vbox.constants.MachineState_SettingUp: u'Configuring',
            vbox.constants.MachineState_Snapshotting: u'Creating Snapshot'
        }
    if id in _ms_text_cache:
        return _ms_text_cache[id]
    else:
        return u'(Unknown)'

_ms_icon_cache = None
def MachineState_icon(id):
    global _ms_icon_cache
    if _ms_icon_cache is None:
        vbox = VBoxWrapper()
        _ms_icon_cache = {
            # There may be better unicode symbols available, but these are
            # ones I found to work even in older/limited terminal fonts.
            vbox.constants.MachineState_Null: ('state error', u'?'),
            vbox.constants.MachineState_PoweredOff: ('state off', u'\u25a0'),
            vbox.constants.MachineState_Saved: ('state off', u'\u25c9'),
            vbox.constants.MachineState_Teleported: ('state off', u'T'),
            vbox.constants.MachineState_Aborted: ('state error', u'!'),
            vbox.constants.MachineState_Running: ('state run', u'\u25b6'),
            vbox.constants.MachineState_Paused: ('state pause', u'\u2225'),
            vbox.constants.MachineState_Stuck: ('state error', u'!'),
            vbox.constants.MachineState_Teleporting: ('state on', u'T'),
            vbox.constants.MachineState_LiveSnapshotting: ('state on', u'S'),
            vbox.constants.MachineState_Starting: ('state on', u'\u25a0'),
            vbox.constants.MachineState_Stopping: ('state pause', u'\u25a0'),
            vbox.constants.MachineState_Saving: ('state pause', u'\u25d4'),
            vbox.constants.MachineState_Restoring: ('state pause', u'\u25d4'),
            vbox.constants.MachineState_TeleportingPausedVM: ('state pause', u'T'),
            vbox.constants.MachineState_TeleportingIn: ('state off', u'T'),
            vbox.constants.MachineState_FaultTolerantSyncing: ('state run', u'\u25e9'),
            vbox.constants.MachineState_DeletingSnapshotOnline: ('state run', u'D'),
            vbox.constants.MachineState_DeletingSnapshotPaused: ('state pause', u'D'),
            vbox.constants.MachineState_OnlineSnapshotting: ('state pause', u'S'),
            vbox.constants.MachineState_RestoringSnapshot: ('state off', u'R'),
            vbox.constants.MachineState_DeletingSnapshot: ('state off', u'D'),
            vbox.constants.MachineState_SettingUp: ('state off', u'\u25a0'),
            vbox.constants.MachineState_Snapshotting: ('state off', u'S')
        }
    if id in _ms_icon_cache:
        return _ms_icon_cache[id]
    else:
        return ('state error', u'?')

_mt_text_cache = None
def MediumType_text(id):
    global _mt_text_cache
    if _mt_text_cache is None:
        vbox = VBoxWrapper()
        _mt_text_cache = {
            vbox.constants.MediumType_Normal: u'Normal',
            vbox.constants.MediumType_Immutable: u'Immutable',
            vbox.constants.MediumType_Writethrough: u'Writethrough',
            vbox.constants.MediumType_Shareable: u'Shareable',
            vbox.constants.MediumType_Readonly: u'Read-Only',
            vbox.constants.MediumType_MultiAttach: u'Multi-Attach'
        }
    if id in _mt_text_cache:
        return _mt_text_cache[id]
    else:
        return u'(Unknown)'

_nadt_text_cache = None
def NetworkAdapterType_text(id):
    global _nadt_text_cache
    if _nadt_text_cache is None:
        vbox = VBoxWrapper()
        _nadt_text_cache = {
            vbox.constants.NetworkAdapterType_Null: u'<Invalid>',
            vbox.constants.NetworkAdapterType_Am79C970A: u'AMD PCNet-PCI II',
            vbox.constants.NetworkAdapterType_Am79C973: u'AMD PCNet-FAST III',
            vbox.constants.NetworkAdapterType_I82540EM: u'Intel PRO/1000 MT Desktop',
            vbox.constants.NetworkAdapterType_I82543GC: u'Intel PRO/1000 T Server',
            vbox.constants.NetworkAdapterType_I82545EM: u'Intel PRO/1000 MT Server',
            vbox.constants.NetworkAdapterType_Virtio: u'Paravirtualized'
        }
    if id in _nadt_text_cache:
        return _nadt_text_cache[id]
    else:
        return u'(Unknown)'

_natt_text_cache = None
def NetworkAttachmentType_text(id):
    global _natt_text_cache
    if _natt_text_cache is None:
        vbox = VBoxWrapper()
        _natt_text_cache = {
            vbox.constants.NetworkAttachmentType_Null: u'',
            vbox.constants.NetworkAttachmentType_NAT: u'NAT',
            vbox.constants.NetworkAttachmentType_Bridged: u'Bridged',
            vbox.constants.NetworkAttachmentType_Internal: u'Internal',
            vbox.constants.NetworkAttachmentType_HostOnly: u'Host-Only',
            vbox.constants.NetworkAttachmentType_Generic: u'Generic',
            vbox.constants.NetworkAttachmentType_NATNetwork: u'NAT Network'
        }
    if id in _natt_text_cache:
        return _natt_text_cache[id]
    else:
        return u'(Unknown)'

_pvp_text_cache = None
def ParavirtProvider_text(id):
    global _pvp_text_cache
    if _pvp_text_cache is None:
        vbox = VBoxWrapper()
        _pvp_text_cache = {
            vbox.constants.ParavirtProvider_None: u'',
            vbox.constants.ParavirtProvider_Default: u'Default',
            vbox.constants.ParavirtProvider_Legacy: u'Legacy',
            vbox.constants.ParavirtProvider_Minimal: u'Minimal',
            vbox.constants.ParavirtProvider_HyperV: u'Hyper-V',
            vbox.constants.ParavirtProvider_KVM: u'KVM'
        }
    if id in _pvp_text_cache:
        return _pvp_text_cache[id]
    else:
        return u'(Unknown)'

_pm_text_cache = None
def PortMode_text(id):
    global _pm_text_cache
    if _pm_text_cache is None:
        vbox = VBoxWrapper()
        _pm_text_cache = {
            vbox.constants.PortMode_Disconnected: u'Disconnected',
            vbox.constants.PortMode_HostPipe: u'Host Pipe',
            vbox.constants.PortMode_HostDevice: u'Host Device',
            vbox.constants.PortMode_RawFile: u'Raw File',
            vbox.constants.PortMode_TCP: u'TCP Socket'
        }
    if id in _pm_text_cache:
        return _pm_text_cache[id]
    else:
        return u'(Unknown)'

_sb_text_cache = None
def StorageBus_text(id):
    global _sb_text_cache
    if _sb_text_cache is None:
        vbox = VBoxWrapper()
        _sb_text_cache = {
            vbox.constants.StorageBus_Null: u'<invalid>',
            vbox.constants.StorageBus_IDE: u'IDE',
            vbox.constants.StorageBus_SATA: u'SATA',
            vbox.constants.StorageBus_SCSI: u'SCSI',
            vbox.constants.StorageBus_Floppy: u'Floppy',
            vbox.constants.StorageBus_SAS: u'SAS',
            vbox.constants.StorageBus_USB: u'USB',
            vbox.constants.StorageBus_PCIe: u'PCIe'
        }
    if id in _sb_text_cache:
        return _sb_text_cache[id]
    else:
        return u'(Unknown)'