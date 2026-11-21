# Public command specification / 公開コマンド仕様
This is public software metadata, not a live browser tool listing. No operation commands are accepted by this server. Runtime schemas from the target page are authoritative. Mutation calls through WebMCP require expectedWorkspaceId and expectedPageInstanceId. The local manual panel inserts current IDs and rejects explicit mismatches.
最新ソフトの公開コマンド仕様です。現在のブラウザの登録状態や制作データではありません。対象画面の一覧・仕様バージョンと照合してください。変更コマンドには対象番号が必要です。手動欄では現在の番号を補い、明示された不一致を拒否します。サーバーにコマンドを送らないでください。
{
  "version": "2.17.0",
  "commands": {
    "studio": [
      {
        "name": "get_studio_guide",
        "description": "Workは初めてこのサイトを起動したらこのガイドを読み、画像を目視して判断する。文字の直線・スプライン、制御点削減、微調整も案内する。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "get_stitch_techniques",
        "description": "図案を見て技法を選ぶため、実装されている機能・対象・操作の違いを読む。適用はWorkがプレビューを見て決める。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "get_generated_files",
        "description": "この画面で生成したファイル名、形式、容量、保存要求を読む。端末への保存は確認できない。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "describe_generated_file",
        "description": "実容量・MIME・SHA-256と転送情報を読む。大きなJSONにはcompression=gzipを推奨。解凍後も元のJSONのまま。blob URLをチャットリンクとして使わない。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "fileId": {
              "type": "string"
            },
            "compression": {
              "type": "string",
              "enum": [
                "none",
                "gzip"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "fileId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "read_generated_file_chunk",
        "description": "生成済みファイルをbase64で最大1MiBずつ取得。describeと同じcompressionでoffset順に復元。gzipは解凍し元容量とSHA-256を照合。取得だけでは添付や保存を意味しない。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "fileId": {
              "type": "string"
            },
            "offset": {
              "type": "integer",
              "minimum": 0
            },
            "length": {
              "type": "integer",
              "minimum": 1,
              "maximum": 1048576
            },
            "compression": {
              "type": "string",
              "enum": [
                "none",
                "gzip"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "fileId",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "acknowledge_chat_file_delivery",
        "description": "全内容の取得・容量とSHA-256照合・ホスト側のチャット添付成功を確認してから呼ぶ。添付能力がない場合は呼ばず理由を報告。保存待ちの入れ替えはこの報告後に進む。端末保存は未確認のまま。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "fileId": {
              "type": "string"
            },
            "sha256": {
              "type": "string",
              "pattern": "^[a-f0-9]{64}$"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "fileId",
            "sha256",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "generate_editable_project",
        "description": "現在の制作状態を復元用.jiminy（gzip圧縮）として生成する。format=jsonで従来形式も選べる。ファイル内容は分割取得で受け取れる。端末保存やチャット添付は別途確認。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "fileName": {
              "type": "string",
              "minLength": 1,
              "maxLength": 80
            },
            "format": {
              "type": "string",
              "enum": [
                "jiminy",
                "json"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "select_delivery_formats",
        "description": "完成後に受け取るJIMINY/JSON/JEF/PES/PEC/DSTを複数選択。生成はまだ行わない。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "formats": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "jiminy",
                  "json",
                  "jef",
                  "pes",
                  "pec",
                  "dst"
                ]
              },
              "minItems": 1,
              "maxItems": 6
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "formats",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "inspect_export_options",
        "description": "選択形式・現在の名前・命名方法・使用済み3桁番号を読む。生成しない。画面未表示なら保存済み設定を返す。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "set_export_naming",
        "description": "チャットで選んだdate（日付）/numbers（001〜999の3桁）/custom（指定名）を画面と同じ処理で設定。numbersは番号省略で未使用番号を選ぶ。使用済みの指定番号は拒否。生成しない。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "mode": {
              "type": "string",
              "enum": [
                "date",
                "numbers",
                "custom"
              ]
            },
            "fileName": {
              "type": "string",
              "minLength": 1,
              "maxLength": 64
            },
            "number": {
              "type": "string",
              "pattern": "^(?!000)[0-9]{3}$"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "mode",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "generate_selected_files",
        "description": "チャットで指定された形式と命名方法を設定後に生成。ユーザーに画面ボタンを押すよう求めない。数字のみは使用済み番号を避け、形式や分割ごとに次の番号へ進む。実ファイル名は生成一覧で確認。チャット添付と端末保存は別。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_preview_background",
        "description": "刺繍プレビューの背景のみ変更する。画像・ステッチ・出力ファイルは変更しない。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "background": {
              "type": "string",
              "enum": [
                "white",
                "light-gray",
                "dark-gray"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "background",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "get_studio_state",
        "description": "画像、色数、島、輪郭、ステッチ、処理中の状態を要約して読む。画像そのものは画面で確認する。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "list_stitch_regions",
        "description": "輪郭抽出後の領域ID、色、設定、概略をページ単位で調べる。島の数は色数とは別。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "ids": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "offset": {
              "type": "integer",
              "minimum": 0
            },
            "limit": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "inspect_island_complexity",
        "description": "解析された島の大きさと色別件数を読み、画像に対して小島が多すぎないか判断する材料を返す。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "inspect_stitch_order",
        "description": "色グループ一覧、または指定グループ内の島ID・位置・順番・中心間移動距離の概算を読む。画像のプレビューと照合する。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "groupKey": {
              "type": "string"
            },
            "offset": {
              "type": "integer",
              "minimum": 0
            },
            "limit": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "focus_stitch_region",
        "description": "島IDを選択して画像上でハイライトする。位置と糸の流れをWorkが画面で確認する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": [
                "string",
                "integer"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_region_base_stitch_enabled",
        "description": "サテンで置き換える文字島の畳縫いを止める。サテン層の針数と文字の形を確認し、再生成する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": [
                "string",
                "integer"
              ]
            },
            "enabled": {
              "type": "boolean"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "enabled",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "reorder_stitch_group",
        "description": "画面の整列と同じ縫い順データを変更する。groupKey内の全島IDを希望する順に指定。中心距離は概算で、変更後に生成・目視確認する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "groupKey": {
              "type": "string"
            },
            "ids": {
              "type": "array",
              "items": {
                "type": [
                  "string",
                  "integer"
                ]
              },
              "minItems": 2,
              "maxItems": 1000
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "groupKey",
            "ids",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "move_stitch_color_group",
        "description": "既存画面の⬆⬇と同じ操作で色グループを一つ前後へ移す。自動整列が有効な場合は再生成時の並びを確認する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "groupKey": {
              "type": "string"
            },
            "direction": {
              "type": "string",
              "enum": [
                "up",
                "down"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "groupKey",
            "direction",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_stitch_auto_sort",
        "description": "手動で決めた色・島の順番を再生成時も維持するには false を選ぶ。画面の自動整列スイッチと同じ状態を変更する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "boolean"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "enabled",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "navigate_studio_stage",
        "description": "指定工程の画面へ移る。前提が未完了なら失敗を返す。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "stage": {
              "type": "string",
              "enum": [
                "input",
                "color",
                "filter",
                "labeling",
                "contour",
                "stitch",
                "export"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "stage",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_color_count",
        "description": "減色画面のスライダーで2〜64色を指定する。実行は別操作。見た目の色数を先に判断する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "count": {
              "type": "integer",
              "minimum": 2,
              "maximum": 64
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "count",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "run_studio_stage",
        "description": "現在の設定で減色・仕上げ・領域・輪郭・ぬいのうち一工程を実行し、完了結果を読む。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "stage": {
              "type": "string",
              "enum": [
                "color",
                "filter",
                "labeling",
                "contour",
                "stitch"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "stage",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "prepare_stitch_export",
        "description": "JEF/PES/PEC/DSTを保存画面で選ぶ。ファイル生成はまだ行わない。PES/PEC/DSTは試験的。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "format": {
              "type": "string",
              "enum": [
                "jef",
                "pes",
                "pec",
                "dst"
              ]
            },
            "fileName": {
              "type": "string",
              "minLength": 1,
              "maxLength": 80
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "format",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "download_stitch_file",
        "description": "準備した形式を生成しブラウザへダウンロードを要求。端末への保存完了は確認できない。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_region_stitch",
        "description": "輪郭IDを指定し、縫い角度、ピッチ、密度または縫い種を変更する。再生成してプレビューで確認する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": [
                "string",
                "integer"
              ]
            },
            "angle": {
              "type": "number",
              "minimum": 0,
              "maximum": 180
            },
            "pitch": {
              "type": "number",
              "minimum": 0.3,
              "maximum": 5
            },
            "density": {
              "type": "number",
              "minimum": 0.3,
              "maximum": 4
            },
            "fillType": {
              "type": "string",
              "enum": [
                "tatami",
                "long-short",
                "spiral",
                "fur",
                "curve-fill",
                "flow-lines"
              ]
            },
            "furStyle": {
              "type": "string",
              "enum": [
                "legacy",
                "fluffy"
              ]
            },
            "flowGuide": {
              "type": "array",
              "items": {
                "type": "number",
                "minimum": -1,
                "maximum": 1
              },
              "minItems": 3,
              "maxItems": 3
            },
            "flowBend": {
              "type": "number",
              "minimum": -1,
              "maximum": 1
            },
            "flowCycles": {
              "type": "number",
              "minimum": 0.25,
              "maximum": 4
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_region_mix_pattern",
        "description": "既存Mix領域のクロスハッチ/平行を変更する。色A/Bが設定済みの領域だけを対象にし、画像とぬい結果を見て選ぶ。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": [
                "string",
                "integer"
              ]
            },
            "pattern": {
              "type": "string",
              "enum": [
                "cross",
                "parallel"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "pattern",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_region_mix_parameters",
        "description": "既存2色Mixの角度、ピッチ、平行パターンの2色間オフセットを調整する。値を変えた案を再生成し画像と比較する。クロスではoffsetMmは適用されない。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": [
                "string",
                "integer"
              ]
            },
            "pattern": {
              "type": "string",
              "enum": [
                "cross",
                "parallel"
              ]
            },
            "density": {
              "type": "number",
              "minimum": 0.2,
              "maximum": 4
            },
            "angle": {
              "type": "number",
              "minimum": 0,
              "maximum": 180
            },
            "offsetMm": {
              "type": "number",
              "minimum": -5,
              "maximum": 5
            },
            "offsetDirection": {
              "type": "number",
              "minimum": 0,
              "maximum": 360
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "create_region_mix",
        "description": "Workが元画像を見て選んだ2色のパレット番号から、指定領域にクロスハッチ/平行Mixを作る。別の糸色が必要なら先に減色を見直す。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": [
                "string",
                "integer"
              ]
            },
            "colorAIndex": {
              "type": "integer",
              "minimum": 0
            },
            "colorBIndex": {
              "type": "integer",
              "minimum": 0
            },
            "pattern": {
              "type": "string",
              "enum": [
                "cross",
                "parallel"
              ]
            },
            "density": {
              "type": "number",
              "minimum": 0.2,
              "maximum": 4
            },
            "angle": {
              "type": "number",
              "minimum": 0,
              "maximum": 180
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "colorAIndex",
            "colorBIndex",
            "pattern",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "inspect_stitch_colors",
        "description": "減色パレットと現在縫う単色グループを区別して読む。元RGB・島ID・選べる糸番号を返す。陰影を画像で確認してから統合する。Mix層は別に確認。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "merge_stitch_colors",
        "description": "現在の単色グループの元RGBから糸番号へ明示的に統合。輪郭・縫わない設定・密度・角度を保持。全指定を検証してから一括適用し一度生成する。自動で影を消さない。Mixやロック中の変更は拒否。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "assignments": {
              "type": "array",
              "minItems": 1,
              "maxItems": 64,
              "items": {
                "type": "object",
                "properties": {
                  "fromColor": {
                    "type": "array",
                    "minItems": 3,
                    "maxItems": 3,
                    "items": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 255
                    }
                  },
                  "toColorCode": {
                    "type": "string"
                  }
                },
                "required": [
                  "fromColor",
                  "toColorCode"
                ],
                "additionalProperties": false
              }
            },
            "generate": {
              "type": "boolean"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "assignments",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "apply_stitch_region_edits",
        "description": "縫わない・色・畳/ロング＆ショート/毛並み/等高線・下縫い・輪郭サテン・2色Mixを一度に設定し、必要なら一度だけ生成する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "operations": {
              "type": "array",
              "minItems": 1,
              "maxItems": 100,
              "items": {
                "type": "object"
              }
            },
            "generate": {
              "type": "boolean"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "operations",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "inspect_import_prompt",
        "description": "画像が選択され、既存作業がある場合に保存/初期化/キャンセルの状態を読む。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "open_stitch_pro",
        "description": "先にStudioで画像・減色・仕上げ・領域・輪郭・基本設定を準備する。図案をサテン／毛並みPROへ渡す正規の入口。PROのURLを直接開くだけでは受け渡されない。移動後は機能一覧と状態を再取得する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "kind": {
              "type": "string",
              "enum": [
                "satin",
                "fur"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "kind",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "resolve_import_prompt",
        "description": "既存データを保存してから新画像へ進む、そのまま初期化、またはキャンセル。画像が選択済みの確認画面だけを操作。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "choice": {
              "type": "string",
              "enum": [
                "save_then_replace",
                "replace_without_save",
                "cancel"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "choice",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "inspect_pro_result",
        "description": "Satin/毛並みデータの追加・入替画面と現在のレイヤー数を読む。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "resolve_pro_result",
        "description": "既存レイヤーへ追加、入替、またはサテン結果の取消を選ぶ。表示中の確認画面にのみ作用する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "kind": {
              "type": "string",
              "enum": [
                "satin",
                "fur"
              ]
            },
            "choice": {
              "type": "string",
              "enum": [
                "merge",
                "replace",
                "cancel"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "kind",
            "choice",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "get_jiminy_guide_catalog",
        "description": "MCPサーバーの最新スキル一覧を取得する。制作データは送信しない。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "get_jiminy_guide",
        "description": "スキルを取得する。まず一覧とtransport-policy、workflowを読み、花と葉はflower-veinsも取得。本文はMCPサーバーに統一。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "topic": {
              "type": "string"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "topic"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "get_workspace_status",
        "description": "現在の画面・WebMCP登録状態・操作一覧を確認",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "get_work_history",
        "description": "このStudioの直近100件の手動・WebMCP操作結果を確認。引数・画像・結果データは記録しない。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "capture_work_preview",
        "description": "現在の刺繍プレビューを取得して目視確認",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "import_stitch_image",
        "description": "ブラウザ内のdata URL画像読込。既存作業の保存確認を省略しない。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "dataUrl": {
              "type": "string"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "dataUrl",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      }
    ],
    "satin": [
      {
        "name": "set_petal_thread_mix",
        "description": "輪郭花びらの糸色と混ざり方を設定。中間色の糸は自動生成しない。中心点・方式・段数は画面で設定し、再生成とプレビュー確認を行う。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "inspect_satin_work",
        "description": "Workはサテン画面を初めて開いたら読む。直線・スプラインの選び方、制御点を減らす判断、目視して微調整する順番を返す。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "list_satin_islands",
        "description": "原図から受け渡された島ID、色、外接矩形、軌道本数を読む。画面で文字かどうか確認する。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "offset": {
              "type": "integer",
              "minimum": 0
            },
            "limit": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "select_satin_island",
        "description": "原図の島をサテン編集対象に選択し、画面に表示する。文字の形を確認する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": [
                "string",
                "integer"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "split_satin_island",
        "description": "Dの縦棒と曲線などを分ける。画面の形を見て島の外から外までの切断線を原図座標で指定する。軌道生成前に実行し、分割後の各島を確認する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": [
                "string",
                "integer"
              ]
            },
            "from": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 2,
              "maxItems": 2
            },
            "to": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 2,
              "maxItems": 2
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "from",
            "to",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "create_satin_trajectory",
        "description": "自動中心線が閉じたループなら保持する。カット後や枝分かれで開いた線は、始点と終点を方向・延長判断に使い、自動曲線を維持する。主線の後はappend:trueで枝を追加。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "start": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 2,
              "maxItems": 2
            },
            "end": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 2,
              "maxItems": 2
            },
            "startRole": {
              "type": "string",
              "enum": [
                "outer",
                "junction"
              ]
            },
            "endRole": {
              "type": "string",
              "enum": [
                "outer",
                "junction"
              ]
            },
            "append": {
              "type": "boolean"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "join_satin_strokes",
        "description": "同じ選択島の軌道IDをつなぐ順に指定。穴や輪郭外を横断する接続は拒否。変更後は再生成する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "ids": {
              "type": "array",
              "items": {
                "type": [
                  "string",
                  "integer"
                ]
              },
              "minItems": 2
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "ids",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_satin_junction",
        "description": "mode=primaryは指定軌道を交差付近で優先。separateは優先を解除して別々に縫う。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "mode": {
              "type": "string",
              "enum": [
                "primary",
                "separate"
              ]
            },
            "primaryId": {
              "type": [
                "string",
                "integer"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "mode",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_satin_stroke_route",
        "description": "Workが元画像を見て中心線を指定。extendStart/extendEnd は外側の自由端だけを輪郭近くまで伸ばす。枝分かれ側は false にする。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "points": {
              "type": "array",
              "minItems": 2,
              "maxItems": 24,
              "items": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                  "type": "number"
                }
              }
            },
            "replace": {
              "type": "boolean"
            },
            "tension": {
              "type": "number",
              "minimum": 0,
              "maximum": 1
            },
            "geometry": {
              "type": "string",
              "enum": [
                "auto",
                "line",
                "spline"
              ]
            },
            "extendStart": {
              "type": "boolean"
            },
            "extendEnd": {
              "type": "boolean"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "points",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_satin_stroke_endpoints",
        "description": "Workが直線筆を指定。枝はreplace:falseで追加し、枝分かれ点を主線の8px以内に置く。外側の自由端だけ輪郭付近まで延長する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "start": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 2,
              "maxItems": 2
            },
            "end": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 2,
              "maxItems": 2
            },
            "startRole": {
              "type": "string",
              "enum": [
                "outer",
                "junction"
              ]
            },
            "endRole": {
              "type": "string",
              "enum": [
                "outer",
                "junction"
              ]
            },
            "replace": {
              "type": "boolean"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "start",
            "end",
            "startRole",
            "endRole",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_satin_trajectory_density",
        "description": "選択島の既存軌道のピッチをmm単位で変更する。サテンを再生成しプレビューを比較する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "densityMm": {
              "type": "number",
              "minimum": 0.1,
              "maximum": 5
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "densityMm",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "simplify_satin_trajectory",
        "description": "自動ボタンで作った点列を間引き、残った点をスプラインの制御点にする。島の外や穴へのはみ出しを検査する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "tolerancePx": {
              "type": "number",
              "minimum": 0.2,
              "maximum": 5
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "tolerancePx",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "generate_selected_satin",
        "description": "既存のサテン生成ボタンを実行し、生成結果と点数を読む。まず軌道を画面で確認する。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "send_satin_to_studio",
        "description": "文字の元の畳縫いを置き換えるならreplaceBase=true。画面で重なりを確認してStudioへ送る。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "replaceBase": {
              "type": "boolean"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "get_jiminy_guide_catalog",
        "description": "MCPサーバーの最新スキル一覧を取得する。制作データは送信しない。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "get_jiminy_guide",
        "description": "スキルを取得する。まず一覧とtransport-policy、workflowを読み、花と葉はflower-veinsも取得。本文はMCPサーバーに統一。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "topic": {
              "type": "string"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "topic"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "get_workspace_status",
        "description": "現在の画面・WebMCP登録状態・操作一覧を確認",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "get_work_history",
        "description": "このStudioの直近100件の手動・WebMCP操作結果を確認。引数・画像・結果データは記録しない。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "capture_work_preview",
        "description": "現在の刺繍プレビューを取得して目視確認",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      }
    ],
    "fur": [
      {
        "name": "inspect_fur_work",
        "description": "毛並みPROの状態と設定を読む",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "includeEditableData": {
              "type": "boolean",
              "description": "falseなら画像・マスク・全方向配列を省略し、設定とくしの変更数だけを軽量取得"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "set_fur_settings",
        "description": "毛並み方式・密度・長さを変更",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "furStyle": {
              "type": "string",
              "enum": [
                "legacy",
                "fluffy",
                "zigzag",
                "contour"
              ]
            },
            "furCenters": {
              "type": "array",
              "maxItems": 100,
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "x": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 1
                  },
                  "y": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 1
                  }
                },
                "required": [
                  "x",
                  "y"
                ],
                "additionalProperties": false
              }
            },
            "contourFurSettings": {
              "type": "object",
              "additionalProperties": false
            },
            "routingMode": {
              "type": "string",
              "enum": [
                "dessin",
                "hair_long",
                "hair_satin"
              ]
            },
            "density": {
              "type": "number",
              "minimum": 1,
              "maximum": 30
            },
            "strokeLength": {
              "type": "number",
              "minimum": 1,
              "maximum": 100
            },
            "wholeForeground": {
              "type": "boolean"
            },
            "furBoundary": {
              "type": "string",
              "enum": [
                "inside",
                "outside"
              ]
            },
            "furOverhang": {
              "type": "number",
              "minimum": 0,
              "maximum": 20
            },
            "zigzagRows": {
              "type": "integer",
              "enum": [
                2,
                3
              ]
            },
            "zigzagSpacing": {
              "type": "number",
              "minimum": 3,
              "maximum": 40
            },
            "zigzagWidth": {
              "type": "number",
              "minimum": 0.05,
              "maximum": 1
            },
            "zigzagOverlap": {
              "type": "number",
              "minimum": 0.1,
              "maximum": 0.8
            },
            "optimizationGoal": {
              "type": "string",
              "enum": [
                "flow",
                "distance"
              ]
            },
            "shortJumpThreshold": {
              "type": "number",
              "minimum": 0,
              "maximum": 10
            },
            "resolutionMode": {
              "type": "string",
              "enum": [
                "basic",
                "detail"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "set_fur_part",
        "description": "足・腕などの部分範囲と毛の設定を登録・選択する。座標は画像に対する0～1。背景や保護部分は生成対象外。",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "name": {
              "type": "string",
              "maxLength": 40
            },
            "rect": {
              "type": "object",
              "properties": {
                "x": {
                  "type": "number",
                  "minimum": 0,
                  "maximum": 1
                },
                "y": {
                  "type": "number",
                  "minimum": 0,
                  "maximum": 1
                },
                "w": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "maximum": 1
                },
                "h": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "maximum": 1
                }
              },
              "required": [
                "x",
                "y",
                "w",
                "h"
              ],
              "additionalProperties": false
            },
            "strokeLength": {
              "type": "number",
              "minimum": 2,
              "maximum": 60
            },
            "zigzagWidth": {
              "type": "number",
              "minimum": 0.05,
              "maximum": 1
            },
            "zigzagSpacing": {
              "type": "number",
              "minimum": 3,
              "maximum": 40
            },
            "furBoundary": {
              "type": "string",
              "enum": [
                "inside",
                "outside"
              ]
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "rect",
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "optimize_fur_stitches",
        "description": "毛並みを最適化してプレビューを更新",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "send_fur_to_studio",
        "description": "毛並みデータをStudioへ返す",
        "readOnly": false,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "expectedWorkspaceId",
            "expectedPageInstanceId"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "get_jiminy_guide_catalog",
        "description": "MCPサーバーの最新スキル一覧を取得する。制作データは送信しない。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "get_jiminy_guide",
        "description": "スキルを取得する。まず一覧とtransport-policy、workflowを読み、花と葉はflower-veinsも取得。本文はMCPサーバーに統一。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "topic": {
              "type": "string"
            },
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [
            "topic"
          ],
          "additionalProperties": false
        }
      },
      {
        "name": "get_workspace_status",
        "description": "現在の画面・WebMCP登録状態・操作一覧を確認",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "get_work_history",
        "description": "このStudioの直近100件の手動・WebMCP操作結果を確認。引数・画像・結果データは記録しない。",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      },
      {
        "name": "capture_work_preview",
        "description": "現在の刺繍プレビューを取得して目視確認",
        "readOnly": true,
        "inputSchema": {
          "type": "object",
          "properties": {
            "expectedWorkspaceId": {
              "type": "string"
            },
            "expectedPageInstanceId": {
              "type": "string"
            }
          },
          "required": [],
          "additionalProperties": false
        }
      }
    ]
  }
}

## 花びらサテンと初心者案内（2.20.0）
Satin画面でapply_petal_preset、set_petal_settings、set_petal_center、generate_petal_satinを追加。例：select_satin_islandで対象を選択→apply_petal_preset {preset:"neat"}→set_petal_center {islandId:<現在の島>,x:<島内px>,y:<島内px>}→generate_petal_satin→inspect_satin_work。操作前に現在のworkspace/page識別子を取得し各変更ツールへ渡す。数値を推測したまま使わず原図・外接矩形・現行schemaを確認。
毛並みPROではset_fur_settings {furStyle:"contour",strokeLength:18,zigzagSpacing:10,zigzagWidth:.8,contourFurSettings:{rows:6,rowGap:8,stagger:.5,centerBlend:.7,direction:"inside"}}は処理画像pxの試作初期候補。set_fur_settingsのfurCentersは0〜1正規化座標。対象や処理解像度で調整し、輪郭を越える場合はfurBoundary/outside・furOverhangと保護を確認。どちらも再生成と拡大検査が必要。リモートMCPはガイド取得のみ。


## PRO比較制作と再接続（2.21.0）
Studioで前処理完了→open_stitch_pro(kind=satin|fur)→ページ移動後にWebMCPツールを再取得→get_workspace_statusで画面・workspaceId・pageInstanceIdを照合する。Satinはselect_satin_island→apply_petal_preset→set_petal_center→set_petal_settings→set_petal_thread_mix→generate_petal_satin→send_satin_to_studio。Furはset_fur_settings→画面の変換を実行・完了確認→send_fur_to_studio。optimize_fur_stitchesは入口なので呼び出しただけで最適化完了と報告しない。
WebMCPのハンドルが失効・別画面を返す場合は再取得する。解消しない場合はソフト内の正式コマンドパネルまたは画面操作を使用し、履歴の「手動」と「WebMCP」を区別する。read_generated_file_chunkはdescribeのfileId・圧縮指定でoffset順に取得し、容量とSHA-256を検証する。保存要求・チャットで受け取れるファイル・利用者端末への保存は別々に報告する。サーバーMCPはガイド読取のみで、Studioの制作データを操作しない。

## 輪郭内になじむつなぎ縫い（2.22.0）
目的はJUMPをゼロにすることではなく、移動の縫いも図案内になじませること。花びらサテンと毛並みPROにtravelMode=off|run|zigzagを追加。初期offで従来の経路を保つ。runは短い走り縫い、zigzagは小さなジグザグの実縫いであり、曲がったJUMPではない。対象内の近い端点へ順序を調整し、元の毛・花びらの向きは反転しない。同じ糸色・元色/島・段の範囲を保護し、輪郭外・穴・消しゴム・選択範囲外を横切る接続は拒否する。短い内側の折れ道も候補にするが、大回りはせず収まらない場合はJUMP。外毛の毛先が輪郭外ならつなぎ縫いの端点にしない。
Satinのset_petal_settings、Furのset_fur_settingsでtravelMode/travelMaxGap/travelWidth/travelPitch/travelBudgetを設定できる。数値は処理画像px。試す初期候補: 最大40px・幅2px・針間隔8px・追加点数上限0.2。解像度/図案寸法で調整し、細い部分はrunまたはoffにする。毛並みは生成で反映、または順序最適化で比較。既存ファイルを読み込むだけでは改善されない。
追加の針目と厚みを増やすため点数予算と同じセルへの集中制限を適用。行き先が近いだけで美観が保証されるわけではない。つなぎが後から覆われる保証もない。JUMP破線とつなぎ縫いを区別し、全体・拡大・再生で顔、穴、余白、重なり順を確認。試し縫い必須。
保存した花の計算比較: /samples/blended-travel/。3色サテンは同じ保存輪郭・設定から再計算してJUMP199→152、47接続、実際の経路点+186。保存した3色毛並み経路はJUMP877→412、465接続、経路点+1161。入口JUMPを含む経路数であり、機械出力の総針数/渡り数ではない。クマの改善結果や試し縫い確認として流用しない。サーバーMCPはガイド取得のみ。

## Vector-aligned large zigzag travel / 針方向に沿う大きなジグザグ移動
travelMode=zigzag は前後の実際の針の往復から向きを推定し、左右の軸を滑らかにつなぐ。移動全体の上限 travelMaxGap は1–300処理画像px、左右の幅 travelWidth は0–60px。travelPitch は1–30pxで移動の刻みと各１針の上限を兼ねる。例180/24/20は花の比較用で、機械の推奨mm値ではない。最終寸法に換算して試し縫いする。
別の島には渡らない。同色でも別島は接続しない。島IDと画像の四方向連結領域、穴、消しゴム、全ての針間の線を保護する。危険な接続はJUMPを残す。大きな移動でも追加点数・重なり上限を維持する。再生成してプレビュー再生で確認する。


## Repeated vector sweeps / 針方向を優先する往復移動
zigzag は各位置で左→右と針方向に沿って往復し、少し前進して繰り返す。１往復で接続完了という制約はない。travelAdvance（0.1–30処理画像px、初期2px）を振り幅travelWidthと１針上限travelPitchから独立して指定する。実効前進量は幅の20%以下にも制限し、戻りの線が斜めに崩れにくくする。前後の針方向は滑らかにつなぐ。多くの往復で点数が増えるためtravelBudget上限は維持する。JUMPが残る理由を点数上限・境界・重なりに分けて説明し、ゼロJUMPを優先しない。Furの数値は倍率換算される。既存ファイルは再生成して確認する。


## Continuous satin movement / 連続サテン移動（試験）
travelMode=satin をSatin set_petal_settings/Fur set_fur_settingsで選ぶ。既存off/run/zigzagは維持。経路は独自のA*による島内の回り込み、針方向と道の長さを考慮した局所順序選択、左右レール往復で構成する。研究のコードやライブラリは取り込んでいない。大域最適や完全被覆の証明はない。
同じ島・糸色・重なり順グループ内で接続。色別指定時は段だけを理由にJUMPで分断しないが、段順指定のorderGroupは維持。閉じた花びら/毛のループは近い線上へ入口を回して向きと全周を保つ。開いた毛は形を欠かさないため始点を維持する。
travelWidth は左右の振り幅、travelAdvance は前進量、travelPitch は１針上限（処理画像px）。穴、消しゴム、輪郭外、別の同色島を横切らない。狭い所は振り幅を縮め、必要なら幅0で通過する。元の輪郭外の毛先が接続端の場合はJUMPが残り得る。
このモードではtravelMaxGap、travelBudgetによる割合打切り、同じセル3回の打切りを使わず、移動も総経路点数totalPointsに含める。無制限計算ではなく、探索/点数上限に達した接続は拒否しunreachableに記録する。JUMPゼロを保証しない。元データを保持し総点数、重なり、全体/拡大/再生、試し縫いを確認。最終JEF/PES針数は書出し後に別途確認。
花の保存済み経路の計算比較：Satin JUMP199→3、総経路点13139。Fur877→25、総43690。実機未確認。比較ページの緑は診断表示で実際の糸色ではない。

2026-10-10 大きな連続サテン移動の比較：travelWidth=168（前回24の7倍）、travelAdvance=28（前回4の7倍）、travelPitch=20（1針上限は別設定）。サテンPRO・毛並みPROとも幅0〜420処理画像pxを指定可能。狭い所は幅を縮めるため実際の幅は場所ごとに異なる。これは1095pxの花での比較値で、全画像共通の推奨値ではない。経路JUMPはSatin199→3、Fur877→26、総経路点数8255/31463。書出し機械針数・実機縫いは未確認。

2026-10-11 針数を抑える比較：幅168・前進28を維持し、travelPitchを20から30処理画像pxへ広げた。移動の折返し位置・線形状・移動距離・JUMP数は同じで、直線上の分割点だけを削減。Satin総経路点8255→5964、Fur31463→23804。最終出力で機械側の最大針長による再分割があれば、この削減率は維持されない。中心の重なり量や糸の厚みそのものを減らす変更ではない。処理画像と刺繍サイズからmm換算し、試し縫いを確認。

2026-10-11 局所方向に合わせた移動：元の針線から近傍8サンプルの軸を計算し途中の方向を優先。左右端の方向が揃い、全幅を保護領域内で振れるときのみサテン往復。短い/縦方向/幅不足はライン。端点の軸の交点へ島内で回り込める場合は折れ点を追加し、穴はA*で複数区間に分ける。局所方向との一致が0.6未満の長いラインは接続を拒否しJUMPを残す。厳密な全交差禁止の証明ではない。開いた毛束は近い終点から反転して全線を保持。別島・穴を横断しない。比較はSatin1692経路点/JUMP38、輪郭毛2101経路点/JUMP38。機械針数ではない。輪郭毛の根元間隔12/段間隔10/18段は処理365pxの花の比較値で全画像推奨ではない。少し疎らにボタンは現在値から根元間隔1.2倍/段間隔1.25倍/段数0.9倍。再生成・全体拡大確認・試し縫いが必要。

2.23.0 一筆サテン（試験）：メイン畳縫いのfur-engine.js内generateRadialSatinClippingを確認し、円弧に沿って内外交互に針を置く考え方を花びら輪郭に応用。set_petal_settingsのoneStroke=true、または花びらパネルの一筆サテンを選ぶ。輪郭・内側専用。生成時に隣の針へ進む連続ジグザグを作り、従来の後付けサテン移動は行わない。同色の隣段へ短く安全に渡れる場合のみ結合。別島・穴・接続不能は経路分割。全体一本や交差ゼロを保証しない。既存の三角方式はoneStroke=falseで保持。糸色は段ごとの振分けで、三角単位ミックスとは異なり色の帯が出やすい。花の比較設定spacing16,length73,rows9,rowGap38（1095px）で786経路点・5経路。機械針数ではなく、実画面と書出し・試し縫いは未確認。

2.23.1 repairLongJump=true：一筆サテンの元の針座標・順序・色を保持し、同色・同島の最長JUMP（100px以上）だけ既存サテン線をたどる島内ステッチへ変更。travelPitchは追加針間隔上限。穴・別島・色替えは縫って横断しない。安全な経路がない場合や探索対象3000点超はJUMP保持。花比較786→800経路点、JUMP5→4。試し縫い未確認。

2.23.2 JUMP限定修正を新規設定で初期ONにする。保存済みの明示的OFFは保持。既存針位置・順序を保ち、移動が周囲の針方向を横切る区間だけ局所針方向に交互に振る。輪郭と穴の安全判定で振幅を縮める。針方向に沿っている移動には余分な横振りを足さない。追加針間隔はtravelPitch上限。花比較の追加点14→38、総経路点800→824。実機の針数ではなく、重なり・厚みは試し縫いで確認。

2.23.3 毛並みPROのサテン・輪郭毛でもrepairLongJump=trueを新規設定で初期ONにする。set_fur_settingsで明示OFF可。furStyle=contour またはroutingMode=hair_satinに限り、通常のtravelModeより優先。生成後の本体と縫い順を保ち、同色・同じ連結島の最長JUMP（処理座標100px以上）一箇所だけ局所針方向へ振る島内移動ステッチに変更。travelPitchはPRO処理座標、表示座標へscaleを一度だけ掛ける。外毛本体を許可していても移動は元の色領域の内側のみ。穴・色別消しゴム・選択除外・外背景を越えず、接続できなければJUMP保持。毛並みPROは経路の先頭をJUMPとして扱うため修正した二経路だけ同じ順序で結合してStudioへ戻す。最適化ボタンでもこの方式がONなら全体を並べ替えずJUMP限定調整。その他の旧毛並みは従来通り。花の計算比較JUMP38→37、2101→2147経路点（46点追加）。実画面操作と機械書出し・試し縫いは未実施。

2.23.4 毛並みPROのrepairLongJump=trueは最長一箇所ではなく、同色・同じ連結島で安全につなげられるJUMPを複数調整する。サテンPRO側は承認済みの最長一箇所方式を保持。毛並み本体・針順・色は不変。各経路は追加済みのつなぎではなく不変の元データから計画し、周囲の針方向へ振る。島外・穴・マスク・別島・色替え・経路なしはJUMP保持。最大200箇所、追加2万経路点の上限。探索対象3000点超の色グループは保持。花計算比較JUMP38→3（入口と2色替え）、35箇所接続、695点追加、2101→2796経路点。追加箇所の厚み・中心重なりは試し縫いで確認。経路点と最終機械針数を区別。

2.23.5 所長の見た目評価により毛並みPROはv182の広いサテン移動へ戻す。専用保持モジュールで幅168・前進28・針間隔20を比較。サテンPROの承認済み一筆サテンとJUMP限定調整は保持。毛並みPROのrepairLongJump=trueという互換設定名は広い移動のONを表す。前の広い移動プリセットボタンで168/28/20を再適用でき、保存済み数値は保持。毛並み本体の形を保ちながら縫い順と移動を計画するため、縫い順を固定する方式ではない。同じ色領域の連結島内だけを移動し、穴・色替え・マスク・外背景は縫って越えない。狭い場所は幅を縮める。比較は当時の保存済み毛並み本体を使用し877→26JUMP、総31463経路点を完全再現。現在の毛並み密度設定を当時に戻す操作ではない。追加点が多くなるので針数・厚み・重なり・縫製時間と試し縫いを確認。機械針数ではない。


## 中心の隙間を補う短い毛・弱いつむじ（2.23.6・試験）
Fur PROのcontourのみ。中心点を単なる収束点でなく短い毛の補完範囲として扱う。通常画面の輪郭毛設定で「中心の隙間を短い毛で埋める」をONにし、中心を埋める半径4〜80、中心の毛の長さ1〜40（いずれも処理画像px）、回す強さ−1〜1を設定する。0は渦なし、負は逆方向。選択した中心ごとに全体値／短い重なり(overlap)／つむじ(whorl)を選べる。旧プロジェクトはcenterFillEnabled=falseで従来形を保持。中心が保護マスクや別色上なら追加しない。千鳥の根元から短い三角毛を出し、外側へ既存毛長に馴染ませ、中心範囲の重複を最寄り中心の担当に分ける。明示的なくしの方向も優先し、目鼻口・穴・消しゴムを保護する。これは2D表現で物理的な毛や実機の縫い上がりではない。
ブラウザWebMCP/手動コマンド set_fur_settings の contourFurSettings に centerFillEnabled/centerFillRadius/centerFillLength/centerFillTwist、furCenters の各点に centerStyle=inherit|overlap|whorl を指定できる。設定後は再生成。補完毛もFur構成リストに保持し、下縫いは通常構成リストへ別途。保存・再編集で設定を保持する。
移動欄「毛の線をたどる移動」(followHairTravel=true)をONにすると、輪郭毛の広いサテン移動より優先し、元の毛の座標・順序を保持したまま既存線と短い10px接続を候補にする。針間隔20px、同じ島・元色・糸色とマスクを保護。大回りは拒否、自然につながらない場合はJUMPを保持。初期OFFで旧設定を変えない。設定は処理画像に対して座標倍率で換算する。JUMPをゼロにする目的ではない。
クマ顔の計算比較 /samples/bear-face/#K : H(中心補完なし)5333縫い点/432JUMP、K(額つむじ・頬耳overlap、半径28/毛10/回転0.2)6333/403、L(半径38/毛12)7268/383。5つの中心点と表の輪郭毛・2色は共通、下縫いなし。生成経路の非JUMP点であり機械形式での最終針数ではない。小さいKから比較し、中心が濃くなりすぎたら半径・長さ・回転を減らす。ブラウザ実操作・実機試し縫いは未確認。公開ガイドとソース内のスナップショットを更新し、インストール済み個人プラグイン本体の更新は別途確認する。サーバーMCPはガイド読取専用。


## 輪郭毛の毛先ゆらぎ・実糸比較（2.23.7・試験）
Fur PRO contourFurSettings.naturalVariation=0〜1。旧データと初期値は0で従来の計算を保持。根元の等間隔配置は保ち、輪郭接線を前後2点の方向と補間して細かな段差をなめらかにする。毛長を最大18%×設定値、向きを最大約4.6度×設定値で決定的に変化させる。毎回ランダムに変わる処理ではない。明示的なくしの強さ1の方向は変えない。長さは境界で切られるため輪郭や段の規則性は残る。目鼻口・穴・マスクを保護する。方向と長さの変更後に必ず再生成し、全体と頬・耳の拡大で比較。
クマM/N案はゆらぎ0.65、中心に合わせる強さ0.8、段間隔10、根元18、長さ34、中心増毛38/12/0.2。左右の頬・耳の中心位置を鏡像にした比較であり、自動左右対称検出ではない。Mはジャノメ214ブラウン1色、Nは205ダークブラウン→214ブラウン→213ベージュ3色。ソフト内のJANOME_THREADS表のRGBを使用し、公式JANOME糸色表 https://www7.janome.co.jp/global/wp-content/uploads/accessoriescatalog.pdf で番号と色名を確認。RGBは実物の色を保証しない。Fur画面の糸候補ボタンで同じRGBを選べるが、実機ファイルの糸番号設定完了を意味しない。Studioで実糸メーカー・番号・左右の共通割当と書き出し番号を確認する。別メーカーはそのメーカーの表で改めて選ぶ。
毛束を1回ずつ指定した1/3色へ分配し、架空の中間色糸は増やさない。色ごとにまとめる縫い順で糸替えを抑えるが重なり順は変わる。試し縫いをする。計算比較 /samples/bear-face/#M と #N はライブ画面制作やJEF/PES出力・試し縫いを行った証明ではない。目鼻口は参考塗り表示。毛先の調整を追加したため点数・JUMPは再計測し、最終ミシン針数と区別する。


## v239 縫い順の向き＋島内ジャンプ補修（試験）
毛並みリズムPROのset_fur_settings、花びらサテンPROのset_petal_settingsでoptimizeRouteDirection:true（初期ON）。既存の連続STITCHを経路として扱い、経路の境目をJUMPと誤認しない。動的計画法で前後の同一ドメイン移動距離を合わせ、短くなる場合だけ経路を逆順にする。経路順・糸色・段・針目の形は保つ。複数段をまたぐ連続経路とdirectionLockedは逆順にしない。色替え時の移動はこの距離集計の対象外。必ずしも最長JUMPが短くなる保証はない。
サテンPROのoneStroke:true、repairLongJump:trueでは最長一箇所だけでなく、同じ糸色・島内の複数JUMPを既存針目のグラフで回り込み、周囲の針方向になじませる。最大200箇所・追加2万点。毛並みPROの輪郭毛でfollowHairTravel:trueとrepairLongJump:trueなら、毛の線をたどる処理のあと同じ補修を適用（最大200箇所・追加2千点）。同RGBでも別の連結島は縫って横断せず、穴・マスク・選択外を避ける。経路がない／上限に達した所はJUMPを残す。内側のつなぎSTITCHと島間の機械JUMPを区別する。画像pxからmmへの縮尺と最終出力の針数を確認。
設定を変えたら再生成。ON/OFFで本体針目・糸色・段順、JUMP、移動距離、追加点数を比較。比較ページ /samples/route-optimization/ は保存された顔の毛データから計算した追加補修で、Studioの画面操作／実機の試し縫い／新JEF書出しは未実施。既存の顔合成JEFは前版のまま。新しい共通処理を畳や走り縫い全般に適用したとは言わない。布の試し縫いが必要。


## v240 複数色の島内JUMP経路／サテンの斜めつなぎ抑止
この項目はv239の複数色・サテンの補修方式を更新する。毛並みPRO set_fur_settings.islandTravelMode は auto / stitch / jump。初期autoは生成結果が1糸色なら従来の島内つなぎ縫い、複数糸色なら輪郭・穴・凹みを避ける針上げの島内JUMP。stitchは旧つなぎ縫い、jumpは1色でも島内JUMP。本体経路の逆順判断は継続する。各糸色の縫い順を保ち、A*の島内経路を移動間隔travelPitchごとの複数JUMPに分ける。追加点はisJump:true,islandJumpWaypoint:true。STITCHを追加せず、JUMP点数が増えても縫う針数の増加とは区別する。連結島・sourceColor・選択マスクを保護。別の島は通常のJUMPで、針上げを禁止すると機械的に移動できない。
サテンPROのrepairLongJump:trueは花びら／一筆サテンのJUMPを同じ島内で回り込ませる。斜めのつなぎSTITCHを追加せず、段の移動も複数JUMPにする。針目の形・色・段順を保つ。追加移動点最大2万、計算で通路が見つからない／上限に達した場合は報告のunreachable,budgetLimitedを見て再調整し、穴横断を解消したと断言しない。島内経路の各直線区間を厳密な輪郭交差／ラスタ境界で検査する。
JUMPは糸切りではない。糸切りなしでは渡り糸が布上に残ることがある。上の糸色で隠れるかはプレビューだけでは保証できず、最終色にも同じ注意。試し縫いで確認する。比較 /samples/route-optimization/ は保存済み毛データを用いた計算試作、画面操作と新JEF出力・実機未実施。一色の計算結果が前版と同一であること、3色の既存STITCH点数が不変で全JUMP区間が島内であること、穴・U字凹み・同RGB別島を検査。


## 採用例と運用判断（2.24.2）
採用済みの顔試作は /samples/bear-face-ready/ 。クマ全身の完成や実機確認を意味しない。
|項目|採用値・判断|
|---|---|
|顔の寸法|73.5×47mm、110mm枠指定の計算試作|
|粗い畳下地|間隔3mm、ピッチ4.5mm、45度。一般には間隔3〜5mmから布と隙間で判断。毛と別層|
|輪郭毛|根元間隔18、段間隔10、段数24、毛長34、幅0.5、千鳥0.5。PRO処理座標でありmmではない|
|方向・自然さ|中心強さ0.8、ゆらぎ0.65。中心増毛半径38、長さ12、回転0.2。額・両頬・両耳の5中心を配置、左右は鏡像|
|移動|optimizeRouteDirection:true、repairLongJump:true、followHairTravel:true、islandTravelMode:auto。短いJUMPの通常接続閾値0|
|M|毛214ブラウン1色。合成JEF 8,574 STITCH、314 JUMP/ゼロ移動、糸替え3回、18,566bytes|
|N|毛205→214→213の3色。合成JEF 8,648 STITCH、1,915 JUMP/ゼロ移動、糸替え5回、25,142bytes|
両案とも顔パーツを含め実糸4種類。JEFのSTITCH数には最後のJUMP後の互換パディングを含む。JUMP点数は針数ではない。連続JUMPの途中に針落ちを挿入しない。
1色の輪郭毛は従来のなじむつなぎ縫い、複数色は島内の針上げ経路を基本にする。花びら／一筆サテンはrepairLongJumpで島内を回り込む。別島を縫って橋渡ししない。unreachable・budgetLimitedが非ゼロなら未解決を報告し、マスクと寸法を確認する。JUMPは糸切りではなく渡り糸が残り得る。
数値を別画像へ丸写ししない。処理画像寸法と完成mmを合わせ、狭い部位は1〜2色へ減らし、左右の糸割当を揃える。くし・中心点を保持して変更後再生成、下地と毛の二重縫い、目鼻口、穴、凹部、最終針数を確認する。試し縫いで密度・引きつれ・渡り糸を確認する。
取得順：catalog→transport-policy→workflow→studio-operation→recipes→quality→command-catalog。サーバーMCPはガイド読取だけ。実操作は選択ページのWebMCPで現在のスキーマを確認し、利用できないコマンドを発明しない。設定変更、生成、保存要求、端末保存確認を区別する。


## 輪郭毛の柔らかさ・細幅・境界検査（2.25.0）
輪郭毛だけの比較ではfurStyle=contourを使う。検証完了前にふわふわ・三角毛を削除せず、旧図案の互換性を保つ。
contourFurSettings.whorlSoftness=0〜1（0で従来）、adaptiveWidth=trueで細い部分の根元幅を縮める。外向きの毛先が収まらない場合は同じ色・保護範囲内の逆方向のみ試す。柔らかさは中心への方向集中と中心増毛の放射を緩める。くしは優先。centerBlend、naturalVariation、短い毛を合わせて全体・顔・足を拡大比較する。
Basicの保護マスクは元画像の対応範囲に保護画素が1点でもあればそのセルを保護する。輪郭毛の消しゴム変更後は線分全体を検査して分割する。最終はDetailでも確認。意図的外毛と保護穴の逸脱を区別する。
移動は既存の方向最適化・島内経路を使う。1色の縫う移動と複数色の島内JUMPを区別し、STITCH/JUMP/移動距離、unreachable/budgetLimitedを確認。ジャンプ数と未糸切りの糸露出は別。島・穴を横切らず離れた島のJUMPを0と約束しない。
AI操作は画面移動後にツール一覧とget_workspace_statusを取り直す。同名登録時・画面終了時は旧登録を解除（対応APIがある場合）。ホストの古いハンドルが直った証拠にはしない。読取→設定→生成→状態・全体/拡大→Studio取込→重複検査→出力。失敗した変更を無条件で再試行しない。
合成細幅テストで従来0点→39点、線分の収容と1画素保護穴の保存を確認。クマの美観や実縫製改善の証拠ではない。

輪郭毛でfollowHairTravelを使い先頭JUMPを縫う移動へ修正した連続経路は、同じ色・sourceColor・幅・島で線分が収容される場合に一本に結合して返す。独立レイヤーの先頭がStudioで再びJUMPになるのを防ぐ。縫う順序と元の点列は維持し、最終routeMetricsとafterJumpsを一致させる。

2.25.1: 新規の選択は毛並み／輪郭毛／サテン／デッサン。旧ふわふわ・三角毛・ミックスは新規候補から外すが、旧プロジェクトの復元・再生成は保持。クマのDetail・1色輪郭毛の実生成では12,149点、STITCH12,148、JUMP1（開始位置への移動）。接続前の312JUMPから減少。元1095画素マスクで縫う12,148線分の保護範囲逸脱0を確認。混合3色とは解像度・設定が違うため同条件比較と呼ばない。実縫製は未検証。


## 輪郭毛の中央の継ぎ目・内毛/外毛（2.26.0）
毛と毛の一般的な隙間と、輪郭から内側へ重ねた段が出会う中央/斜めの継ぎ目を区別する。contourFurSettings.seamFillEnabledは2.26.0では初期OFF。2.26.1から新規は初期ON、保存済みのOFFは維持。OFFではv204の毛の生成と同一。ONでは同じ色・選択・消しゴムの保護範囲の内側だけに短い毛を追加し、既存の根元/毛先/くし/段数/糸色を変更しない。中心点から放射するcenterFillとは別。
seamFillWidth=1〜20（既定6）、seamFillLength=1〜40（既定8）、seamFillSpacing=2〜20（既定4）。単位はPRO処理座標。「中央の白線を補う（標準）」は幅10・長さ8・間隔4を設定してONにする。方向は近傍毛の軸を平均し、明示的なくしを優先。線分全体が同じ色・保護範囲内か検査し、追加毛の重複を抑える。穴・顔・肉球などの別領域は補わない。白線が必ず消える、布が必ず隠れるとは約束せず、密度/重なり/点数/JUMPを全体と拡大で比較する。
「輪郭内版」はfurBoundary=inside、furOverhang=0、edgeBridge=0。「少し外毛版」はfurBoundary=outside、furOverhang=3、edgeBridge=0。境界以外の設定と中心/くし/グラデーションは保持する。外毛は背景につながる外側だけへ許可し、内側の穴を外背景として扱わない。外周の別色の線が毛先を止める場合、edgeBridgeの幅を別に調整して、顔・穴への影響を再確認する。自動でその線を越えない。
四角の合成形状で基準510点、標準補い付き内毛594点、外毛612点を比較。これは低密度のアルゴリズム検査でありクマの最終針数ではない。OFFの完全一致、明示的なくし、再現性、外毛の上限、保護穴、3色の保持をテスト。実際のStudio→PRO受け渡しでクマも確認し、旧レイヤーを追加重複させず比較用コピーに置換する。試し縫いは別途必要。
MCPサーバーは公開ガイドの取得専用。seamFill設定を含む制作操作はページのWebMCPまたは画面操作で行い、図案・画面IDをMCPサーバーへ送らない。

2.26.1 中央のランダム補毛：新規・空の設定ではseamFillEnabled=true、seamFillJitter=.35。保存済みのseamFillEnabled=falseと、v204以前の既存輪郭設定（フラグ未保存）はOFFを維持。seamFillJitter=0〜1、0で規則的。標準ボタンは幅10・長さ8・間隔4・ランダム.35。中央の短い毛だけに、根元位置・長さ・向きの小さな固定乱数のゆらぎを加える。再生成で同じ形を再現する。強さ1のくしの方向にはランダムな回転を加えない。既存輪郭毛は変えない。保護境界内の近い補毛だけを連続経路へまとめ、穴や別色を横切る接続を作らない。補毛ON時の毛をたどる探索は、従来の迂回上限を満たせない高コスト領域だけ早めに打ち切る。受理される経路の形は保持する。生成量・JUMP・重なりは再確認。
