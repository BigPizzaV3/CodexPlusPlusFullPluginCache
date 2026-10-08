plugin:
  id: fuji-x100vi-look-emulator
  name: Fuji X100VI Look Emulator
  version: 0.1.0
  category: image-transformation
  summary: >
    Recebe uma imagem e a recria como se tivesse sido capturada
    com uma Fujifilm X100VI, preservando composição e conteúdo,
    mas substituindo o look de smartphone/computacional por uma
    renderização fotográfica inspirada na X100VI.

  objective: >
    Transformar imagens enviadas pelo usuário em imagens com
    aparência realista de captura Fujifilm X100VI, com ênfase em:
    cor orgânica, sombras mais profundas, highlights mais suaves,
    menor aparência de HDR de celular, nitidez menos artificial
    e atmosfera fotográfica.

  target_use_cases:
    - transformar fotos de celular em fotos com look Fuji X100VI
    - emular renderização Fuji em cenas internas
    - emular renderização Fuji em cenas externas
    - melhorar stills de mesa/objetos com look mais fotográfico
    - criar consistência visual para creators que gostam do look Fuji

  non_goals:
    - não redesenhar a cena
    - não virar filtro vintage pesado
    - não transformar a imagem em ilustração
    - não trocar identidade de pessoas ou objetos
    - não inventar elementos desnecessários

  inputs:
    required:
      - name: input_image
        type: image
        description: >
          Imagem principal enviada pelo usuário. Pode ser uma foto
          de celular, câmera ou frame.
    optional:
      - name: mode
        type: enum
        values:
          - auto
          - indoor
          - outdoor
          - tabletop
          - low_light
        default: auto
        description: >
          Define o tipo de cena ou deixa o plugin detectar automaticamente.

      - name: strength
        type: enum
        values:
          - subtle
          - balanced
          - strong
        default: balanced
        description: >
          Define a intensidade da emulação visual.

      - name: preserve_composition
        type: boolean
        default: true
        description: >
          Mantém enquadramento, posição dos objetos e geometria da cena.

      - name: preserve_text
        type: boolean
        default: true
        description: >
          Tenta preservar textos legíveis presentes na imagem.

      - name: custom_profile
        type: string
        default: default_x100vi
        description: >
          Permite no futuro escolher perfis diferentes.
          Ex.: default_x100vi, ronald_reference_profile, reala_ace_style.

      - name: reference_images
        type: image[]
        max_items: 8
        required: false
        description: >
          Referências opcionais para calibrar ainda melhor o resultado.
          Pode incluir fotos reais da X100VI.

  outputs:
    - name: transformed_image
      type: image
      description: >
        Imagem final recriada com estética Fuji X100VI.

    - name: transform_metadata
      type: object
      description: >
        Metadados descritivos do que o plugin aplicou.
      schema:
        detected_scene_type: string
        applied_profile: string
        strength: string
        preserved_composition: boolean
        notes: string

  visual_signature:
    tone:
      - reduced_smartphone_hdr
      - deeper_cleaner_shadows
      - softer_highlight_rolloff
      - more_atmospheric_midtones

    color:
      - warm_organic_rendering
      - richer_reds
      - richer_oranges
      - better_wood_tones
      - slightly_subdued_natural_greens
      - cohesive_palette

    detail:
      - less_aggressive_digital_sharpening
      - more_organic_microcontrast
      - subtle_realistic_texture
      - optional_light_grain_when_appropriate

    rendering:
      - natural_lens_like_look
      - believable_subject_separation
      - non_computational_depth
      - realistic_camera_feel

    mood:
      - more_photographic
      - more_intentional
      - more_filmic_without_fake_retro_filter

  scene_profiles:
    auto:
      description: >
        Detecta o tipo de cena e escolhe automaticamente o melhor comportamento.

    indoor:
      description: >
        Reforça aconchego, luz prática, sombras mais profundas e calor cromático.
      adjustments:
        - warm_tone_bias
        - softer_highlights
        - moody_shadow_depth
        - practical_light_glow
        - reduced_flattening

    outdoor:
      description: >
        Controla brilho duro, reduz a cara de HDR e harmoniza tons naturais.
      adjustments:
        - control_harsh_sunlight
        - reduce_artificial_green_cast
        - smoother_highlights
        - cleaner_contrast
        - organic_daylight_rendering

    tabletop:
      description: >
        Otimizado para mesas, objetos, papelaria, café, still life.
      adjustments:
        - material_texture_emphasis
        - refined_tonal_rendering
        - warmth_for_objects
        - reduced_sharpening
        - subtle_depth_enhancement

    low_light:
      description: >
        Preserva o clima escuro sem superlimpar a imagem.
      adjustments:
        - keep_night_mood
        - gentle_noise_texture
        - protect_light_sources
        - avoid_overcorrection
        - stronger_atmosphere

  strength_profiles:
    subtle:
      description: >
        Mudança leve, boa para quem quer pouca intervenção.
      multiplier:
        tone: 0.6
        color: 0.6
        detail: 0.5
        mood: 0.5

    balanced:
      description: >
        Perfil padrão. Emulação visível, mas natural.
      multiplier:
        tone: 1.0
        color: 1.0
        detail: 1.0
        mood: 1.0

    strong:
      description: >
        Emulação mais marcada, sem perder realismo.
      multiplier:
        tone: 1.35
        color: 1.25
        detail: 1.15
        mood: 1.25

  processing_pipeline:
    - step: ingest
      description: >
        Recebe a imagem principal e parâmetros opcionais.

    - step: analyze_scene
      description: >
        Analisa iluminação, tipo de cena, HDR excessivo,
        nitidez digital, profundidade aparente e paleta.

    - step: choose_profile
      description: >
        Seleciona automaticamente ou usa o mode informado.

    - step: build_transform_prompt
      description: >
        Constrói um prompt para o Images 2.5 com base na
        assinatura visual da X100VI e no tipo de cena.

    - step: render_with_images_2_5
      description: >
        Recria a imagem preservando a cena original, mas com
        visual calibrado para parecer uma captura Fuji X100VI.

    - step: package_output
      description: >
        Retorna a imagem transformada e metadados do processo.

  system_prompt: |
    You are an image transformation agent specialized in recreating uploaded
    photos as if they were captured with a Fujifilm X100VI.

    Your task is not to redesign the scene. Your task is to preserve the original
    image content while changing its photographic rendering.

    Always preserve:
    - framing
    - composition
    - geometry
    - perspective
    - subject placement
    - object placement
    - environment identity
    - important text when possible

    Always transform the rendering toward a Fujifilm X100VI look:
    - less smartphone-like HDR
    - deeper, cleaner shadows
    - softer and smoother highlight roll-off
    - warm, organic color rendering
    - richer reds, oranges, and wood tones
    - more natural, slightly subdued greens
    - more cohesive overall palette
    - less aggressive digital sharpening
    - more organic microcontrast
    - subtle realistic texture or grain where appropriate
    - natural lens-like rendering
    - atmospheric, believable photographic output

    The result must feel realistic and elegant.
    Do not over-stylize.
    Do not apply a heavy retro filter.
    Do not convert the image into an illustration.
    Do not significantly change scene layout or identity.

  prompt_template: |
    Edit Image A and recreate the exact same scene as if it had been photographed
    with a Fujifilm X100VI.

    Preserve the original framing, composition, perspective, geometry, subject placement,
    object placement, and scene identity. Do not significantly rearrange or invent new elements.

    Apply a Fujifilm X100VI-style photographic rendering with:
    - reduced smartphone HDR appearance
    - deeper, cleaner shadows
    - softer and smoother highlight roll-off
    - warm, organic color rendering
    - richer reds, oranges, and wood tones
    - more natural, slightly subdued greens
    - cohesive overall palette
    - less aggressive digital sharpening
    - more organic microcontrast
    - subtle realistic texture or grain
    - natural photographic depth and lens-like rendering
    - atmospheric, refined, believable camera output

    If the image is indoor, emphasize cozy warmth, practical-light glow, and moodier tonal depth.
    If the image is outdoor, preserve natural daylight while controlling harsh highlights and artificial-looking color.
    If the image is a tabletop or object scene, emphasize refined detail, material texture, and balanced warmth.

    Keep the result realistic, elegant, and believable, like a true Fujifilm X100VI capture.
    Do not make it look like a heavy preset or retro filter.

  api_surface:
    endpoints:
      - method: POST
        path: /transform
        description: >
          Transforma uma imagem no look Fuji X100VI.
        request_schema:
          type: object
          properties:
            input_image:
              type: string
              description: URL ou file reference da imagem
            mode:
              type: string
              enum: [auto, indoor, outdoor, tabletop, low_light]
            strength:
              type: string
              enum: [subtle, balanced, strong]
            preserve_composition:
              type: boolean
            preserve_text:
              type: boolean
            custom_profile:
              type: string
            reference_images:
              type: array
              items:
                type: string
          required:
            - input_image

        response_schema:
          type: object
          properties:
            transformed_image:
              type: string
              description: URL ou file reference da imagem final
            transform_metadata:
              type: object
              properties:
                detected_scene_type:
                  type: string
                applied_profile:
                  type: string
                strength:
                  type: string
                preserved_composition:
                  type: boolean
                notes:
                  type: string

      - method: POST
        path: /calibrate-profile
        description: >
          Futuro endpoint opcional para calibrar um perfil com base
          em pares de referência iPhone/Fuji.
        request_schema:
          type: object
          properties:
            reference_pairs:
              type: array
              items:
                type: object
                properties:
                  source_image:
                    type: string
                  target_fuji_image:
                    type: string
          required:
            - reference_pairs

  default_profile:
    id: default_x100vi
    description: >
      Perfil base derivado da análise visual de amostras Fuji X100VI.
    characteristics:
      warmth: medium
      shadow_depth: medium_high
      highlight_softness: high
      hdr_reduction: high
      sharpening_reduction: medium
      organic_microcontrast: medium_high
      grain: subtle
      color_cohesion: high

  future_profiles:
    - id: ronald_reference_profile
      description: >
        Perfil calibrado especificamente com as referências do usuário.

    - id: reala_ace_style
      description: >
        Variante mais neutra e refinada, inspirada em resultados tipo Reala Ace.

    - id: classic_negative_style
      description: >
        Variante mais contrastada e com caráter mais forte.

  acceptance_criteria:
    - a composição da cena deve permanecer reconhecível
    - a foto final deve parecer menos “smartphone HDR”
    - as sombras devem ter mais profundidade sem perder legibilidade essencial
    - os highlights devem ficar mais suaves
    - o resultado deve parecer fotográfico e realista
    - a imagem não deve parecer filtro exagerado
    - objetos, pessoas e textos importantes devem ser preservados sempre que possível

  failure_conditions:
    - mudança excessiva na composição
    - troca de objetos ou inventar elementos irrelevantes
    - resultado com aparência de filtro fake
    - perda da identidade geral da cena
    - nitidez excessiva ou artificial
    - cores exageradamente saturadas ou irreais

  example_request:
    endpoint: /transform
    body:
      input_image: "file://user_upload.jpg"
      mode: "auto"
      strength: "balanced"
      preserve_composition: true
      preserve_text: true
      custom_profile: "default_x100vi"

  example_response:
    transformed_image: "file://output_fuji_x100vi.jpg"
    transform_metadata:
      detected_scene_type: "indoor"
      applied_profile: "default_x100vi"
      strength: "balanced"
      preserved_composition: true
      notes: "Applied warm indoor tonal shaping, reduced HDR look, softened highlights and added organic contrast."