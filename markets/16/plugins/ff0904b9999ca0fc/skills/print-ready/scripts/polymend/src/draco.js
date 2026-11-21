// This edition does not include the decoder for Draco-compressed GLB files.
export async function decodeDraco() {
  throw new Error('This GLB file is Draco-compressed, which this edition of Polymend does not unpack. Repair it at https://polymend.xyz (in your browser, nothing uploaded), or export it from your 3D app without compression.');
}
