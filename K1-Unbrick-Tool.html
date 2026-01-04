<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>K1 Partition Generator</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #121212; color: #e0e0e0; padding: 20px; display: flex; flex-direction: column; align-items: center; }
        .card { background: #1e1e1e; padding: 25px; border-radius: 12px; border: 1px solid #333; width: 100%; max-width: 550px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        h2 { color: #ff9800; margin-top: 0; border-bottom: 1px solid #333; padding-bottom: 10px; }
        .input-group { margin-bottom: 15px; }
        label { display: block; color: #888; margin-bottom: 5px; font-size: 0.9em; }
        input { width: 100%; padding: 10px; background: #2b2b2b; border: 1px solid #444; border-radius: 4px; color: #00ff00; font-family: monospace; box-sizing: border-box; }
        input:focus { border-color: #ff9800; outline: none; }
        .btn { width: 100%; padding: 12px; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; margin-top: 10px; transition: 0.2s; }
        .btn-load { background: #444; color: white; }
        .btn-gen { background: #ff9800; color: #000; font-size: 1.1em; }
        .btn:hover { opacity: 0.9; }
        .warning { color: #ff5252; font-size: 0.8em; margin-top: 15px; border: 1px solid #ff5252; padding: 10px; border-radius: 4px; }
    </style>
</head>
<body>

<div class="card">
    <h2>K1 Identity Generator</h2>
    
    <div class="input-group">
        <label>Load Existing (Optional):</label>
        <input type="file" id="loadFile" style="color:#888">
    </div>

    <hr style="border:0; border-top:1px solid #333; margin:20px 0;">

    <div class="input-group">
        <label>Serial Number (14 chars):</label>
        <input type="text" id="sn" placeholder="78779428000000" maxlength="14">
    </div>
    <div class="input-group">
        <label>MAC Address (12 chars, no colons):</label>
        <input type="text" id="mac" placeholder="FCEE28000000" maxlength="12">
    </div>
    <div class="input-group">
        <label>Model Name:</label>
        <input type="text" id="model" value="CR-K1">
    </div>
    <div class="input-group">
        <label>Mainboard ID:</label>
        <input type="text" id="board" value="CR4CU220812S12">
    </div>
    <div class="input-group">
        <label>Structure Ver (0=V1, 1=V2/Unicorn):</label>
        <input type="text" id="struct" value="0" maxlength="1">
    </div>

    <button class="btn btn-gen" onclick="generateFile()">Download new sn_mac.img</button>

    <div class="warning">
        <b>CAUTION:</b> Flashing a modified file to <code>/dev/mmcblk0p2</code> can disconnect your printer from Creality Cloud or cause boot issues if formatted incorrectly.
    </div>
</div>

<script>
    // Logic to parse existing file
    document.getElementById('loadFile').addEventListener('change', function(e) {
        const reader = new FileReader();
        reader.onload = function() {
            const str = new TextDecoder().decode(new Uint8Array(reader.result).slice(0, 128));
            const p = str.split(';');
            if(p[0]) document.getElementById('sn').value = p[0];
            if(p[1]) document.getElementById('mac').value = p[1];
            if(p[2]) document.getElementById('model').value = p[2];
            if(p[3]) document.getElementById('board').value = p[3];
            if(p[6]) document.getElementById('struct').value = p[6];
        };
        reader.readAsArrayBuffer(this.files[0]);
    });

    function generateFile() {
        const sn = document.getElementById('sn').value;
        const mac = document.getElementById('mac').value;
        const model = document.getElementById('model').value;
        const board = document.getElementById('board').value;
        const struct = document.getElementById('struct').value;

        // Construct the string: SN;MAC;MODEL;BOARD;PCBA;MACHINE_SN;STRUCT
        // We leave PCBA and Machine_SN empty (just semicolons) per your dump
        const identityString = `${sn};${mac};${model};${board};;;${struct};;`;
        
        // Create 1MB buffer (1024 * 1024 bytes)
        const size = 1024 * 1024;
        const buffer = new Uint8Array(size);
        
        // Convert string to bytes and place at start of buffer
        for (let i = 0; i < identityString.length; i++) {
            buffer[i] = identityString.charCodeAt(i);
        }

        // Trigger Download
        const blob = new Blob([buffer], { type: "application/octet-stream" });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "sn_mac.img";
        link.click();
    }
</script>

</body>
</html>
