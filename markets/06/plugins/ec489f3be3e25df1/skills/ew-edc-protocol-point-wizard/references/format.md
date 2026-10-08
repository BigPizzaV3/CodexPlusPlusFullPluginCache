# 匯入格式 v1

JSON 根：`{"schema":"ew-edc.modbus-tcp/v1","devices":[...]}`。

每個設備：name（設備名稱）、ip（明確 IPv4）、port（1–65535）、unitId（0–255）、brand、model、channels。
每個通道：name、quantity、unit、functionCode（3或4）、address（零起算0–65535）、manualAddress（手冊原字串）、addressBasis（protocol-zero-based）、dataType、registerCount、byteOrder、pollSeconds（1–86400整數）、slope、offset、source（文件頁碼與確認紀錄）、exampleRaw、exampleEngineering、confirmed（布林）。缺漏保持 null，confirmed=false，匯入會阻擋部署。

| 資料型態 | 暫存器數 | 位元組順序 |
|---|---|---|
| int16 / uint16 | 1 | AB、BA |
| int32 / uint32 / float32 | 2 | ABCD、BADC、CDAB、DCBA |
| float64 | 4 | ABCDEFGH、HGFEDCBA、BADCFEHG、GHEFCDAB |

暫存器數由型態決定，不能和文件相矛盾。實際 EDC 版本若未提供所需解析選項會停止，而不猜其他值。採樣秒數由使用者確認。倍率與偏移量須通過範例驗算；範例不是即時量測值。

Excel 工作表「部署點表」的第一列依序為：
設備名稱、IP位址、通訊埠、站號、品牌、型號、通道名稱、物理量、單位、功能碼、協定起始位址、手冊位址、位址基準、資料型態、暫存器數、位元組順序、採樣秒數、倍率、偏移量、來源、原始值範例、工程值範例、已確認。

一個通道一列，同設備的連線欄位一致；「已確認」填是／否。同批最多100設備、1000通道。只支援.xlsx，不支援.xls。樣本 example-draft.json 使用保留示範位址且 confirmed=false，不能直接部署；不是實際協議證據。
