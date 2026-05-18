# apply-taxonomy-nextcloud.ps1
# Creates NZRT 000XXX category tags + all descriptive tags in Nextcloud system tags.
# Method: uploads PHP script via WebDAV, runs server-side MySQL INSERT IGNORE, deletes script.
# Idempotent: INSERT IGNORE skips existing tags, never deletes.
# DB: nzrtnetw_nc | user: nzrtnetw_wp | table: oc_systemtag
# WebDAV: \\nzrtnetwork.com@SSL@2078\DavWWWRoot\cloud.nzrtnetwork.com\
# Run URL: https://cloud.nzrtnetwork.com/<scriptname>.php
#
# Usage: .\apply-taxonomy-nextcloud.ps1

$webdavDest = "\\nzrtnetwork.com@SSL@2078\DavWWWRoot\cloud.nzrtnetwork.com\nctags_run.php"
$runUrl     = "https://cloud.nzrtnetwork.com/nctags_run.php"

$taxonomy = [ordered]@{
    "000API" = @("x402","micropayments","usdc","base-network","flask","python","income","rest-api")
    "000BCH" = @("blockchain","ethereum","base","smart-contracts","rwa","tokenization","web3","defi","wallet")
    "000CLA" = @("ai","agents","llm","claude-code","anthropic","automation","ceo-agent","prompt")
    "000CPL" = @("hosting","cpanel","hoopla","ssl","dns","cron","ci-cd","production")
    "000DOL" = @("erp","crm","invoicing","products","accounting","hr","purchase","reports","finance")
    "000GIT" = @("git","version-control","repository","ci-cd","actions","workflow","automation","pull-request")
    "000ICS" = @("consulting","proptech","defi","enterprise-architecture","commercial","ics","billable")
    "000INF" = @("hosting","dns","ssl","subdomains","server","backup","deployment","infrastructure")
    "000ITE" = @("hardware","patent","rwa","tokenization","iteasel","product","base","ethereum","ite")
    "000K8S" = @("kubernetes","kagent","minikube","container","orchestration","helm","k8s","local")
    "000LLM" = @("ai","prompt","rag","tool-use","skills","cowork","llm","fine-tuning","embedding")
    "000MAI" = @("email","exim","dovecot","imap","smtp","self-hosted","mail","mx")
    "000MST" = @("vault","master","nzrt","obsidian","schema","meta","documentation")
    "000NCL" = @("collaboration","cloud","self-hosted","webdav","caldav","files","sharing","nextcloud")
    "000NCS" = @("charitable","ncs","grants","new-zealand","schools","kura","community","ngo")
    "000OBS" = @("knowledge-base","wiki","docs","sop","markdown","vault","obsidian")
    "000SCR" = @("automation","pipeline","python","powershell","agents","react-agent","mail-handler","scripts")
    "000TOG" = @("enterprise-architecture","adm","archimate","governance","togaf","framework","adr")
    "000WIN" = @("windows-11","laragon","local","runtime","powershell","wamp","dev-environment")
    "000WOR" = @("cms","php","theme","plugin","rest-api","laragon","wamp","wordpress","smart-slider")
}

# Build unique tag list
$allTags = [System.Collections.Generic.List[string]]@()
foreach ($code in $taxonomy.Keys) { $allTags.Add($code) }
foreach ($tags in $taxonomy.Values) {
    foreach ($t in $tags) { if ($allTags -notcontains $t) { $allTags.Add($t) } }
}

# Build PHP tag array literal
$phpArray = ($allTags | ForEach-Object { "'$($_ -replace "'","\\'")'," }) -join "`n    "

$php = @"
<?php
`$pdo = new PDO('mysql:host=localhost;dbname=nzrtnetw_nc;charset=utf8mb4', 'nzrtnetw_wp', 'NZRTnetwork75@');
`$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
`$tags = [
    $phpArray
];
`$stmt = `$pdo->prepare("INSERT IGNORE INTO oc_systemtag (name, visibility, editable) VALUES (?, 1, 1)");
`$created = 0;
foreach (`$tags as `$tag) { `$stmt->execute([`$tag]); if (`$stmt->rowCount() > 0) `$created++; }
echo "Created: `$created\n\n";
foreach (`$pdo->query("SELECT id, name FROM oc_systemtag ORDER BY name")->fetchAll(PDO::FETCH_ASSOC) as `$r) {
    echo `$r['id'] . "\t" . `$r['name'] . "\n";
}
"@

$tmpFile = "$env:TEMP\nctags_run.php"
[System.IO.File]::WriteAllText($tmpFile, $php, [System.Text.Encoding]::UTF8)

Write-Host "Uploading via WebDAV..."
Copy-Item $tmpFile $webdavDest -Force

Write-Host "Running on server..."
$result = Invoke-RestMethod -Uri $runUrl -Method GET -TimeoutSec 30
$result

Write-Host "Deleting from server..."
Remove-Item $webdavDest -Force
Write-Host "Done."
