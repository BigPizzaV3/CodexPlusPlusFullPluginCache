param(
    [Parameter(Mandatory = $true)][ValidateSet("get", "store", "delete")][string]$Action,
    [Parameter(Mandatory = $true)][string]$Service,
    [Parameter(Mandatory = $true)][string]$Account
)

$source = @'
using System;
using System.Runtime.InteropServices;

public static class EmpireCredentialManager {
    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    private struct CREDENTIAL {
        public UInt32 Flags;
        public UInt32 Type;
        public string TargetName;
        public string Comment;
        public System.Runtime.InteropServices.ComTypes.FILETIME LastWritten;
        public UInt32 CredentialBlobSize;
        public IntPtr CredentialBlob;
        public UInt32 Persist;
        public UInt32 AttributeCount;
        public IntPtr Attributes;
        public string TargetAlias;
        public string UserName;
    }

    [DllImport("advapi32.dll", EntryPoint = "CredWriteW", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern bool CredWrite(ref CREDENTIAL credential, UInt32 flags);

    [DllImport("advapi32.dll", EntryPoint = "CredReadW", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern bool CredRead(string target, UInt32 type, UInt32 flags, out IntPtr credential);

    [DllImport("advapi32.dll", EntryPoint = "CredDeleteW", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern bool CredDelete(string target, UInt32 type, UInt32 flags);

    [DllImport("advapi32.dll", SetLastError = false)]
    private static extern void CredFree(IntPtr buffer);

    public static void Store(string target, string account, string secret) {
        byte[] bytes = System.Text.Encoding.Unicode.GetBytes(secret);
        IntPtr blob = Marshal.AllocCoTaskMem(bytes.Length);
        try {
            Marshal.Copy(bytes, 0, blob, bytes.Length);
            CREDENTIAL credential = new CREDENTIAL {
                Type = 1,
                TargetName = target,
                CredentialBlobSize = (UInt32)bytes.Length,
                CredentialBlob = blob,
                Persist = 2,
                UserName = account
            };
            if (!CredWrite(ref credential, 0)) {
                throw new System.ComponentModel.Win32Exception(Marshal.GetLastWin32Error());
            }
        } finally {
            byte[] zeros = new byte[bytes.Length];
            Marshal.Copy(zeros, 0, blob, zeros.Length);
            Marshal.FreeCoTaskMem(blob);
        }
    }

    public static string Read(string target) {
        IntPtr pointer;
        if (!CredRead(target, 1, 0, out pointer)) {
            int error = Marshal.GetLastWin32Error();
            if (error == 1168) return null;
            throw new System.ComponentModel.Win32Exception(error);
        }
        try {
            CREDENTIAL credential = (CREDENTIAL)Marshal.PtrToStructure(pointer, typeof(CREDENTIAL));
            if (credential.CredentialBlob == IntPtr.Zero || credential.CredentialBlobSize == 0) return null;
            return Marshal.PtrToStringUni(credential.CredentialBlob, (int)credential.CredentialBlobSize / 2);
        } finally {
            CredFree(pointer);
        }
    }

    public static bool Delete(string target) {
        if (CredDelete(target, 1, 0)) return true;
        int error = Marshal.GetLastWin32Error();
        if (error == 1168) return false;
        throw new System.ComponentModel.Win32Exception(error);
    }
}
'@

Add-Type -TypeDefinition $source
$target = "$Service/$Account"

if ($Action -eq "store") {
    $secret = [Console]::In.ReadToEnd()
    if ([string]::IsNullOrEmpty($secret)) { exit 2 }
    [EmpireCredentialManager]::Store($target, $Account, $secret)
    exit 0
}

if ($Action -eq "get") {
    $secret = [EmpireCredentialManager]::Read($target)
    if ($null -eq $secret) { exit 1 }
    [Console]::Out.Write($secret)
    exit 0
}

$deleted = [EmpireCredentialManager]::Delete($target)
if ($deleted) { exit 0 }
exit 1
