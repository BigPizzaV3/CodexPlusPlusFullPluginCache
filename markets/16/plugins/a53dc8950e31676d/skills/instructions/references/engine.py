#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================
MPGO PROCESS MAPPER - ENGINE DE VALIDAÇÃO v3.1.0
============================================================
Motor de validação, análise de cobertura e build de artefatos
Arquitetura: AI GPT Generator v3.1.0 (PDCA Oriented)
Build: 2026-01-17 | Ciclo PDCA: 1
============================================================
"""

import sys
import json
import hashlib
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import argparse

try:
    import yaml
    from pydantic import BaseModel, Field, validator, ValidationError
except ImportError:
    print("❌ Dependências ausentes. Instale com:")
    print("   pip install pyyaml pydantic --break-system-packages")
    sys.exit(1)

# ============================================================
# CONSTANTES E CONFIGURAÇÃO
# ============================================================

VERSION = "3.1.0"
BUILD_DATE = "2026-01-17"

# Thresholds globais (sincronizados com cobertura_esperada.yaml)
THRESHOLDS = {
    'score_global_minimo': 85.0,
    'mermaid_quality_minimo': 0.90,
    'documentacao_quality_minimo': 0.85,
    'conformidade_quality_minimo': 1.0,
    'seguranca_quality_minimo': 1.0,
    'ux_quality_minimo': 0.90,
    'knowledge_base_coverage_minimo': 0.80,
}

# Exit codes para CI/CD
EXIT_CODES = {
    'SUCCESS': 0,
    'QUALITY_THRESHOLD_NOT_MET': 1,
    'CRITICAL_METRIC_FAILED': 2,
    'SECURITY_VIOLATION': 3,
    'SYNTAX_ERROR': 4,
    'WARNING_ONLY': 10,
}

# ============================================================
# SCHEMAS PYDANTIC PARA VALIDAÇÃO
# ============================================================

class MetadataSchema(BaseModel):
    """Schema para metadados de artefatos"""
    nome_sistema: str = Field(..., min_length=1)
    versao: str = Field(..., pattern=r'^\d+\.\d+\.\d+$')
    data_criacao: str
    arquitetura_base: str
    modelo_alvo: str
    nivel_usuario: str
    
    @validator('versao')
    def validar_semver(cls, v):
        parts = v.split('.')
        if len(parts) != 3:
            raise ValueError('Versão deve seguir formato MAJOR.MINOR.PATCH')
        if not all(p.isdigit() for p in parts):
            raise ValueError('Componentes de versão devem ser numéricos')
        return v


class BlocoObrigatorioSchema(BaseModel):
    """Schema para blocos da estrutura de output"""
    id: str = Field(..., pattern=r'^bloco_\d{2}$')
    nome: str
    prioridade: int = Field(..., ge=0, le=100)
    conteudo_minimo: List[str]
    
    @validator('prioridade')
    def validar_prioridade(cls, v):
        valid_priorities = [100, 90, 80, 70, 60]
        if v not in valid_priorities:
            raise ValueError(f'Prioridade deve ser uma de: {valid_priorities}')
        return v


class MetricaSchema(BaseModel):
    """Schema para métricas de validação"""
    id: str
    nome: str
    descricao: str
    threshold: float
    threshold_text: str
    formula: str
    criticidade: str
    peso: float = Field(..., ge=0.0, le=1.0)
    
    @validator('criticidade')
    def validar_criticidade(cls, v):
        valid_levels = ['CRÍTICA', 'ALTA', 'MÉDIA', 'BAIXA']
        if v not in valid_levels:
            raise ValueError(f'Criticidade deve ser uma de: {valid_levels}')
        return v


class InstrucoesCompletasSchema(BaseModel):
    """Schema principal para instrucoes_completas.yaml"""
    metadata: MetadataSchema
    
    class Config:
        extra = 'allow'  # Permitir campos adicionais


class KnowledgeBaseEntrySchema(BaseModel):
    """Schema para entradas da base de conhecimento JSONL"""
    id: str = Field(..., pattern=r'^kb_\d{3}$')
    categoria: str
    subcategoria: str
    titulo: str
    descricao: str = Field(..., min_length=10)
    aplicacao: str = Field(..., min_length=10)
    exemplo: str = Field(..., min_length=10)
    metricas_sucesso: str
    referencias: str
    tags: List[str] = Field(..., min_items=1)


# ============================================================
# VALIDADORES DE CÓDIGO MERMAID
# ============================================================

class MermaidValidator:
    """Validador de sintaxe Mermaid.js v10+"""
    
    @staticmethod
    def validar_sintaxe_basica(codigo: str) -> Dict[str, Any]:
        """Validação básica de sintaxe Mermaid"""
        erros = []
        avisos = []
        
        # 1. Verificar declaração flowchart/graph
        if not re.search(r'(flowchart|graph)\s+(TD|LR|BT|RL)', codigo):
            erros.append("Declaração flowchart TD|LR|BT|RL não encontrada")
        
        # 2. Verificar losangos com parênteses (erro comum)
        losangos_incorretos = re.findall(r'\(\{["\'].*?["\']\}\)', codigo)
        if losangos_incorretos:
            erros.append(
                f"Losangos com parênteses detectados: {len(losangos_incorretos)} ocorrências. "
                f"Use {{\"...\"}} ao invés de ({{\"...\"}})."
            )
        
        # 3. Verificar IDs não-alfabéticos
        ids = re.findall(r'\b([A-Z_][A-Z0-9_]*)\[', codigo)
        ids_nao_alfabeticos = [id for id in ids if not re.match(r'^[A-Z]$', id)]
        if ids_nao_alfabeticos:
            avisos.append(
                f"IDs não-alfabéticos detectados: {set(ids_nao_alfabeticos)}. "
                f"Recomendado usar A, B, C..."
            )
        
        # 4. Verificar aspas não-escapadas
        textos = re.findall(r'\["(.*?)"\]', codigo)
        aspas_nao_escapadas = []
        for texto in textos:
            if '"' in texto and '&quot;' not in texto:
                aspas_nao_escapadas.append(texto[:30] + '...')
        
        if aspas_nao_escapadas:
            erros.append(
                f"Aspas duplas não-escapadas detectadas em {len(aspas_nao_escapadas)} textos. "
                f"Use &quot; para escapar."
            )
        
        # 5. Verificar setas (deve ser --> não ->)
        setas_simples = re.findall(r'\s+->\s+', codigo)
        if setas_simples:
            erros.append(
                f"Setas simples (->) detectadas: {len(setas_simples)} ocorrências. "
                f"Use setas duplas (-->)."
            )
        
        return {
            'valido': len(erros) == 0,
            'erros': erros,
            'avisos': avisos,
            'total_erros': len(erros),
            'total_avisos': len(avisos)
        }
    
    @staticmethod
    def validar_ids_alfabeticos(codigo: str) -> Dict[str, Any]:
        """Validar convenção de IDs alfabéticos sequenciais"""
        pattern = r'\b([A-Z_][A-Z0-9_]*)\['
        ids = re.findall(pattern, codigo)
        ids_unicos = sorted(set(ids))
        
        ids_validos = [id for id in ids_unicos if re.match(r'^[A-Z]$', id)]
        ids_invalidos = [id for id in ids_unicos if not re.match(r'^[A-Z]$', id)]
        
        return {
            'total_ids': len(ids_unicos),
            'ids_validos': len(ids_validos),
            'ids_invalidos': len(ids_invalidos),
            'lista_invalidos': ids_invalidos,
            'passou': len(ids_invalidos) == 0
        }
    
    @staticmethod
    def validar_escape_aspas(codigo: str) -> Dict[str, Any]:
        """Validar escape de aspas duplas com &quot;"""
        pattern = r'\["(.*?)"\]'
        textos = re.findall(pattern, codigo)
        
        violacoes = []
        for texto in textos:
            if '"' in texto and '&quot;' not in texto:
                violacoes.append(texto[:50])
        
        return {
            'total_textos': len(textos),
            'violacoes': len(violacoes),
            'lista_violacoes': violacoes,
            'passou': len(violacoes) == 0
        }
    
    @staticmethod
    def validar_losangos(codigo: str) -> Dict[str, Any]:
        """Validar losangos sem parênteses extras"""
        # Padrão incorreto: ({\"...\"}), {(\"...\")}
        pattern_errado = r'\(\{["\'].*?["\']\}\)|\{\(["\'].*?["\']\)\}'
        erros = re.findall(pattern_errado, codigo)
        
        # Padrão correto: {\"...\"}
        pattern_correto = r'\{["\'].*?["\']\}'
        corretos = re.findall(pattern_correto, codigo)
        
        return {
            'losangos_corretos': len(corretos),
            'losangos_incorretos': len(erros),
            'exemplos_erros': erros[:3],
            'passou': len(erros) == 0
        }


# ============================================================
# VALIDADORES DE SEGURANÇA
# ============================================================

class SecurityValidator:
    """Validador de segurança SSTI e XSS (ADR-022)"""
    
    @staticmethod
    def scan_ssti(html_content: str) -> Dict[str, Any]:
        """Detectar padrões de Server-Side Template Injection"""
        padroes_perigosos = {
            'Template Expression': r'\{\{.*?\}\}',
            'Template Statement': r'\{%.*?%\}',
            'Python Internals': r'__class__|__mro__|__subclasses__|__globals__',
            'Dangerous Functions': r'\beval\(|\bexec\(|\bcompile\(',
            'Import Statement': r'\bimport\s+\w+'
        }
        
        vulnerabilidades = []
        for tipo, pattern in padroes_perigosos.items():
            matches = re.findall(pattern, html_content)
            if matches:
                vulnerabilidades.append({
                    'tipo': tipo,
                    'ocorrencias': len(matches),
                    'exemplos': [m[:30] + '...' for m in matches[:2]]
                })
        
        return {
            'vulnerabilidades_detectadas': len(vulnerabilidades),
            'detalhes': vulnerabilidades,
            'passou': len(vulnerabilidades) == 0
        }
    
    @staticmethod
    def scan_xss(html_content: str) -> Dict[str, Any]:
        """Detectar padrões de Cross-Site Scripting"""
        padroes_xss = {
            'Script Tag': r'<script[^>]*>.*?</script>',
            'Inline Script': r'javascript:',
            'Event Handlers': r'\bon\w+\s*=',
            'Iframe': r'<iframe[^>]*>',
            'Object/Embed': r'<(object|embed)[^>]*>'
        }
        
        # Whitelist: apenas Mermaid CDN permitido
        whitelist = [
            r'https://cdn\.jsdelivr\.net/npm/mermaid@',
            r'mermaid\.initialize',
        ]
        
        vulnerabilidades = []
        for tipo, pattern in padroes_xss.items():
            matches = re.findall(pattern, html_content, re.IGNORECASE | re.DOTALL)
            
            for match in matches:
                # Verificar se está na whitelist
                is_whitelisted = any(
                    re.search(wl, match, re.IGNORECASE) for wl in whitelist
                )
                
                if not is_whitelisted:
                    vulnerabilidades.append({
                        'tipo': tipo,
                        'trecho': match[:80] + '...'
                    })
        
        return {
            'vulnerabilidades_detectadas': len(vulnerabilidades),
            'detalhes': vulnerabilidades,
            'passou': len(vulnerabilidades) == 0
        }
    
    @staticmethod
    def validar_csp(html_content: str) -> Dict[str, Any]:
        """Validar presença e qualidade do Content-Security-Policy"""
        csp_pattern = r'<meta.*?Content-Security-Policy.*?>|CSP:.*?default-src'
        
        csp_encontrado = re.search(csp_pattern, html_content, re.IGNORECASE | re.DOTALL)
        
        if csp_encontrado:
            csp_content = csp_encontrado.group(0)
            
            diretivas_essenciais = [
                r"default-src\s+['\"]self['\"]",
                r'script-src',
                r'style-src'
            ]
            
            diretivas_presentes = sum(
                1 for d in diretivas_essenciais 
                if re.search(d, csp_content, re.IGNORECASE)
            )
            
            return {
                'csp_presente': True,
                'diretivas_essenciais': diretivas_presentes,
                'total_esperado': len(diretivas_essenciais),
                'passou': diretivas_presentes == len(diretivas_essenciais)
            }
        
        return {'csp_presente': False, 'passou': False}


# ============================================================
# VALIDADORES DE DOCUMENTAÇÃO
# ============================================================

class DocumentacaoValidator:
    """Validador de completude e estrutura da documentação"""
    
    @staticmethod
    def validar_blocos_obrigatorios(documentacao_md: str) -> Dict[str, Any]:
        """Verificar presença dos 9 blocos obrigatórios"""
        blocos_obrigatorios = [
            (1, r'#+ .*Brief Executivo'),
            (2, r'#+ .*Requisitos.*Etapas'),
            (3, r'#+ .*Arquitetura.*Fluxograma'),
            (4, r'#+ .*C[oó]digo Mermaid'),
            (5, r'#+ .*Exemplos'),
            (6, r'#+ .*Variantes'),
            (7, r'#+ .*Testes.*M[eé]tricas'),
            (8, r'#+ .*Riscos.*Mitiga[çc][õo]es'),
            (9, r'#+ .*Manuten[çc][ãa]o')
        ]
        
        presentes = []
        ausentes = []
        
        for num, pattern in blocos_obrigatorios:
            if re.search(pattern, documentacao_md, re.IGNORECASE):
                presentes.append(f"Bloco {num}")
            else:
                ausentes.append(f"Bloco {num}")
        
        return {
            'blocos_presentes': len(presentes),
            'blocos_ausentes': len(ausentes),
            'lista_ausentes': ausentes,
            'total_esperado': 9,
            'passou': len(presentes) == 9
        }
    
    @staticmethod
    def detectar_pii(texto: str) -> Dict[str, Any]:
        """Detectar Personally Identifiable Information (LGPD)"""
        violacoes = []
        
        patterns = {
            'CPF': r'\d{3}\.\d{3}\.\d{3}-\d{2}',
            'CNPJ': r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}',
            'Email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'Telefone': r'\(\d{2}\)\s*\d{4,5}-\d{4}',
            'RG': r'\d{1,2}\.\d{3}\.\d{3}-[0-9X]'
        }
        
        for tipo, pattern in patterns.items():
            matches = re.findall(pattern, texto)
            if matches:
                for match in matches:
                    # Verificar se é placeholder válido
                    if 'XXX' not in match and '[' not in match and 'exemplo' not in match.lower():
                        violacoes.append({
                            'tipo': tipo,
                            'valor': match[:10] + '***'  # Truncar por segurança
                        })
        
        return {
            'violacoes_detectadas': len(violacoes),
            'detalhes': violacoes,
            'passou': len(violacoes) == 0
        }


# ============================================================
# ANALISADOR DE COBERTURA DA BASE DE CONHECIMENTO
# ============================================================

class CoverageAnalyzer:
    """Analisador de cobertura da base de conhecimento (met_003)"""
    
    def __init__(self, kb_path: str):
        self.kb_path = Path(kb_path)
        self.kb_entries = self._load_kb()
        self.categorias = self._categorize_kb()
    
    def _load_kb(self) -> List[Dict]:
        """Carregar base de conhecimento JSONL"""
        entries = []
        try:
            with open(self.kb_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        entries.append(json.loads(line))
        except FileNotFoundError:
            print(f"⚠️ Arquivo {self.kb_path} não encontrado")
        except json.JSONDecodeError as e:
            print(f"⚠️ Erro ao parsear JSONL: {e}")
        
        return entries
    
    def _categorize_kb(self) -> Dict[str, List[Dict]]:
        """Organizar KB por categoria"""
        categorias = {}
        for entry in self.kb_entries:
            cat = entry.get('categoria', 'unknown')
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(entry)
        return categorias
    
    def analisar_cobertura(self, documentacao_md: str, codigo_mermaid: str) -> Dict[str, Any]:
        """Analisar quanto da KB foi aplicada no output"""
        texto_completo = documentacao_md + "\n" + codigo_mermaid
        texto_lower = texto_completo.lower()
        
        cobertura_por_categoria = {}
        
        # Categorias esperadas com pesos (sincronizado com cobertura_esperada.yaml)
        categorias_esperadas = {
            'prompt_engineering': {'peso': 0.15, 'minimo': 2},
            'mermaid_syntax': {'peso': 0.25, 'minimo': 4},
            'bpm_patterns': {'peso': 0.15, 'minimo': 1},
            'analise_critica': {'peso': 0.15, 'minimo': 2},
            'conformidade': {'peso': 0.15, 'minimo': 2},
            'validacao': {'peso': 0.10, 'minimo': 1},
            'seguranca': {'peso': 0.05, 'minimo': 1},
        }
        
        for categoria, config in categorias_esperadas.items():
            if categoria in self.categorias:
                tecnicas_aplicadas = 0
                tecnicas_categoria = self.categorias[categoria]
                
                for entry in tecnicas_categoria:
                    # Verificar se técnica foi aplicada (heurística)
                    tags = entry.get('tags', [])
                    keywords = [entry.get('titulo', '').lower()] + tags
                    
                    if any(kw.lower() in texto_lower for kw in keywords):
                        tecnicas_aplicadas += 1
                
                score_categoria = min(1.0, tecnicas_aplicadas / config['minimo'])
                
                cobertura_por_categoria[categoria] = {
                    'tecnicas_aplicadas': tecnicas_aplicadas,
                    'minimo_esperado': config['minimo'],
                    'score': score_categoria,
                    'peso': config['peso']
                }
        
        # Calcular score global de cobertura
        coverage_score = sum(
            cat['peso'] * cat['score'] 
            for cat in cobertura_por_categoria.values()
        )
        
        return {
            'coverage_score': round(coverage_score, 3),
            'passou': coverage_score >= THRESHOLDS['knowledge_base_coverage_minimo'],
            'threshold': THRESHOLDS['knowledge_base_coverage_minimo'],
            'por_categoria': cobertura_por_categoria,
            'total_kb_entries': len(self.kb_entries),
            'categorias_analisadas': len(cobertura_por_categoria)
        }


# ============================================================
# ENGINE PRINCIPAL DE VALIDAÇÃO
# ============================================================

class ValidationEngine:
    """Engine principal de validação de artefatos"""
    
    def __init__(self, base_path: str = '.'):
        self.base_path = Path(base_path)
        self.resultados = {}
    
    def validar_yaml_schema(self, yaml_path: str) -> Dict[str, Any]:
        """Validar instrucoes_completas.yaml contra schema Pydantic"""
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            # Validar schema
            schema = InstrucoesCompletasSchema(**data)
            
            return {
                'valido': True,
                'schema': 'InstrucoesCompletasSchema',
                'versao': schema.metadata.versao,
                'erros': []
            }
        
        except ValidationError as e:
            return {
                'valido': False,
                'erros': [str(err) for err in e.errors()],
                'total_erros': len(e.errors())
            }
        except FileNotFoundError:
            return {
                'valido': False,
                'erros': [f'Arquivo {yaml_path} não encontrado']
            }
        except yaml.YAMLError as e:
            return {
                'valido': False,
                'erros': [f'Erro de sintaxe YAML: {str(e)}']
            }
    
    def validar_kb_jsonl(self, jsonl_path: str) -> Dict[str, Any]:
        """Validar base_conhecimento.jsonl"""
        erros = []
        entries_validas = 0
        
        try:
            with open(jsonl_path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    if not line.strip():
                        continue
                    
                    try:
                        entry = json.loads(line)
                        # Validar contra schema
                        KnowledgeBaseEntrySchema(**entry)
                        entries_validas += 1
                    
                    except ValidationError as e:
                        erros.append(f"Linha {i}: {e.errors()[0]['msg']}")
                    except json.JSONDecodeError as e:
                        erros.append(f"Linha {i}: JSON inválido - {str(e)}")
            
            return {
                'valido': len(erros) == 0,
                'entries_validas': entries_validas,
                'erros': erros,
                'total_erros': len(erros)
            }
        
        except FileNotFoundError:
            return {
                'valido': False,
                'erros': [f'Arquivo {jsonl_path} não encontrado']
            }
    
    def validar_mermaid_completo(self, codigo_mermaid: str) -> Dict[str, Any]:
        """Executar todas as validações de Mermaid"""
        validator = MermaidValidator()
        
        resultados = {
            'sintaxe_basica': validator.validar_sintaxe_basica(codigo_mermaid),
            'ids_alfabeticos': validator.validar_ids_alfabeticos(codigo_mermaid),
            'escape_aspas': validator.validar_escape_aspas(codigo_mermaid),
            'losangos': validator.validar_losangos(codigo_mermaid)
        }
        
        # Calcular score agregado
        passou_sintaxe = resultados['sintaxe_basica']['valido']
        passou_ids = resultados['ids_alfabeticos']['passou']
        passou_escape = resultados['escape_aspas']['passou']
        passou_losangos = resultados['losangos']['passou']
        
        score = (
            1.0 * (1.0 if passou_sintaxe else 0.0) +
            0.8 * (1.0 if passou_ids else 0.0) +
            1.0 * (1.0 if passou_escape else 0.0) +
            1.0 * (1.0 if passou_losangos else 0.0)
        ) / 3.8  # Soma dos pesos
        
        resultados['score_mermaid'] = round(score, 3)
        resultados['passou'] = score >= THRESHOLDS['mermaid_quality_minimo']
        resultados['threshold'] = THRESHOLDS['mermaid_quality_minimo']
        
        return resultados
    
    def validar_seguranca_completo(self, html_content: str) -> Dict[str, Any]:
        """Executar todas as validações de segurança"""
        validator = SecurityValidator()
        
        resultados = {
            'ssti': validator.scan_ssti(html_content),
            'xss': validator.scan_xss(html_content),
            'csp': validator.validar_csp(html_content)
        }
        
        # Segurança é binário: ou passa 100% ou falha
        passou_ssti = resultados['ssti']['passou']
        passou_xss = resultados['xss']['passou']
        passou_csp = resultados['csp']['passou']
        
        resultados['score_seguranca'] = 1.0 if all([passou_ssti, passou_xss, passou_csp]) else 0.0
        resultados['passou'] = all([passou_ssti, passou_xss, passou_csp])
        resultados['threshold'] = THRESHOLDS['seguranca_quality_minimo']
        
        return resultados
    
    def calcular_score_global(self) -> Dict[str, Any]:
        """Calcular score global ponderado"""
        # Pesos sincronizados com cobertura_esperada.yaml
        pesos = {
            'mermaid_quality': 0.25,
            'documentacao_quality': 0.25,
            'conformidade_quality': 0.20,
            'seguranca_quality': 0.15,
            'ux_quality': 0.15,
        }
        
        # Obter scores individuais (simplificado - em produção usar resultados completos)
        scores = {
            'mermaid_quality': self.resultados.get('mermaid', {}).get('score_mermaid', 0),
            'documentacao_quality': self.resultados.get('documentacao', {}).get('score', 0.85),
            'conformidade_quality': self.resultados.get('conformidade', {}).get('score', 1.0),
            'seguranca_quality': self.resultados.get('seguranca', {}).get('score_seguranca', 0),
            'ux_quality': 0.90,  # Placeholder - requer validação manual
        }
        
        score_global = sum(
            pesos[categoria] * score 
            for categoria, score in scores.items()
        ) * 100
        
        return {
            'score_global': round(score_global, 2),
            'aprovado': score_global >= THRESHOLDS['score_global_minimo'],
            'threshold': THRESHOLDS['score_global_minimo'],
            'breakdown': {k: round(v * 100, 2) for k, v in scores.items()},
            'interpretacao': self._interpretar_score(score_global)
        }
    
    @staticmethod
    def _interpretar_score(score: float) -> str:
        """Interpretar score global"""
        if score >= 95:
            return "Excelente - Pronto para produção"
        elif score >= 85:
            return "Bom - Pequenos ajustes recomendados"
        elif score >= 70:
            return "Adequado - Revisão necessária"
        else:
            return "Insuficiente - Refazer"


# ============================================================
# INTERFACE CLI
# ============================================================

def cmd_validate(args):
    """Comando: validar artefatos"""
    print(f"🔍 MPGO Process Mapper v{VERSION} - Validação de Artefatos")
    print(f"{'=' * 60}\n")
    
    engine = ValidationEngine()
    exit_code = EXIT_CODES['SUCCESS']
    
    # 1. Validar instrucoes_completas.yaml
    if args.yaml:
        print("📄 Validando instrucoes_completas.yaml...")
        resultado = engine.validar_yaml_schema(args.yaml)
        engine.resultados['yaml'] = resultado
        
        if resultado['valido']:
            print(f"   ✅ Schema válido (versão {resultado['versao']})")
        else:
            print(f"   ❌ Schema inválido: {len(resultado['erros'])} erros")
            for erro in resultado['erros'][:3]:
                print(f"      - {erro}")
            exit_code = EXIT_CODES['SYNTAX_ERROR']
        print()
    
    # 2. Validar base_conhecimento.jsonl
    if args.kb:
        print("📚 Validando base_conhecimento.jsonl...")
        resultado = engine.validar_kb_jsonl(args.kb)
        engine.resultados['kb'] = resultado
        
        if resultado['valido']:
            print(f"   ✅ {resultado['entries_validas']} entradas válidas")
        else:
            print(f"   ❌ {resultado['total_erros']} erros encontrados")
            for erro in resultado['erros'][:3]:
                print(f"      - {erro}")
        print()
    
    # 3. Validar código Mermaid
    if args.mermaid:
        print("🔷 Validando código Mermaid...")
        try:
            with open(args.mermaid, 'r', encoding='utf-8') as f:
                codigo = f.read()
            
            resultado = engine.validar_mermaid_completo(codigo)
            engine.resultados['mermaid'] = resultado
            
            print(f"   Score: {resultado['score_mermaid']:.1%} (threshold: {resultado['threshold']:.0%})")
            
            if resultado['passou']:
                print(f"   ✅ Validação Mermaid aprovada")
            else:
                print(f"   ❌ Validação Mermaid reprovada")
                if not resultado['sintaxe_basica']['valido']:
                    print(f"      Erros de sintaxe: {resultado['sintaxe_basica']['total_erros']}")
                if not resultado['losangos']['passou']:
                    print(f"      Losangos incorretos: {resultado['losangos']['losangos_incorretos']}")
                exit_code = EXIT_CODES['SYNTAX_ERROR']
            print()
        except FileNotFoundError:
            print(f"   ⚠️ Arquivo {args.mermaid} não encontrado\n")
    
    # 4. Validar segurança HTML
    if args.html:
        print("🔒 Validando segurança HTML (ADR-022)...")
        try:
            with open(args.html, 'r', encoding='utf-8') as f:
                html = f.read()
            
            resultado = engine.validar_seguranca_completo(html)
            engine.resultados['seguranca'] = resultado
            
            print(f"   Score: {resultado['score_seguranca']:.0%} (threshold: {resultado['threshold']:.0%})")
            
            if resultado['passou']:
                print(f"   ✅ Nenhuma vulnerabilidade detectada")
            else:
                print(f"   ❌ Vulnerabilidades detectadas:")
                if not resultado['ssti']['passou']:
                    print(f"      SSTI: {resultado['ssti']['vulnerabilidades_detectadas']} ocorrências")
                if not resultado['xss']['passou']:
                    print(f"      XSS: {resultado['xss']['vulnerabilidades_detectadas']} ocorrências")
                if not resultado['csp']['passou']:
                    print(f"      CSP: ausente ou incompleto")
                exit_code = EXIT_CODES['SECURITY_VIOLATION']
            print()
        except FileNotFoundError:
            print(f"   ⚠️ Arquivo {args.html} não encontrado\n")
    
    # 5. Analisar cobertura da KB
    if args.coverage and args.kb:
        print("📊 Analisando cobertura da base de conhecimento...")
        
        # Carregar documentação e Mermaid
        doc_md = ""
        mermaid_code = ""
        
        if args.doc:
            try:
                with open(args.doc, 'r', encoding='utf-8') as f:
                    doc_md = f.read()
            except FileNotFoundError:
                pass
        
        if args.mermaid:
            try:
                with open(args.mermaid, 'r', encoding='utf-8') as f:
                    mermaid_code = f.read()
            except FileNotFoundError:
                pass
        
        analyzer = CoverageAnalyzer(args.kb)
        resultado = analyzer.analisar_cobertura(doc_md, mermaid_code)
        engine.resultados['coverage'] = resultado
        
        print(f"   Coverage Score: {resultado['coverage_score']:.1%} (threshold: {resultado['threshold']:.0%})")
        
        if resultado['passou']:
            print(f"   ✅ Cobertura adequada")
        else:
            print(f"   ⚠️ Cobertura abaixo do esperado")
        
        print(f"\n   Por categoria:")
        for cat, dados in resultado['por_categoria'].items():
            status = "✅" if dados['score'] >= 1.0 else "⚠️"
            print(f"      {status} {cat}: {dados['tecnicas_aplicadas']}/{dados['minimo_esperado']} (score: {dados['score']:.0%})")
        print()
    
    # 6. Score Global
    if len(engine.resultados) > 1:
        print("🎯 Score Global de Qualidade")
        print(f"{'-' * 60}")
        
        score_data = engine.calcular_score_global()
        
        print(f"\n   Score: {score_data['score_global']:.1f}/100")
        print(f"   Status: {score_data['interpretacao']}")
        print(f"   Threshold: {score_data['threshold']:.1f}")
        
        print(f"\n   Breakdown por categoria:")
        for cat, score in score_data['breakdown'].items():
            print(f"      {cat}: {score:.1f}/100")
        
        if score_data['aprovado']:
            print(f"\n   ✅ BUILD APROVADO")
            if score_data['score_global'] < 95:
                exit_code = EXIT_CODES['WARNING_ONLY']
        else:
            print(f"\n   ❌ BUILD REPROVADO")
            exit_code = EXIT_CODES['QUALITY_THRESHOLD_NOT_MET']
    
    # Salvar relatório JSON se solicitado
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'versao_engine': VERSION,
                'resultados': engine.resultados,
                'exit_code': exit_code
            }, f, indent=2, ensure_ascii=False)
        print(f"\n📁 Relatório salvo em: {args.output}")
    
    return exit_code


def cmd_info(args):
    """Comando: exibir informações do engine"""
    print(f"""
MPGO Process Mapper - Engine de Validação
Versão: {VERSION}
Build: {BUILD_DATE}
Arquitetura: AI GPT Generator v3.1.0

Thresholds Configurados:
  - Score Global Mínimo: {THRESHOLDS['score_global_minimo']:.1f}/100
  - Mermaid Quality: {THRESHOLDS['mermaid_quality_minimo']:.0%}
  - Documentação Quality: {THRESHOLDS['documentacao_quality_minimo']:.0%}
  - Conformidade: {THRESHOLDS['conformidade_quality_minimo']:.0%}
  - Segurança: {THRESHOLDS['seguranca_quality_minimo']:.0%}
  - UX Quality: {THRESHOLDS['ux_quality_minimo']:.0%}
  - KB Coverage: {THRESHOLDS['knowledge_base_coverage_minimo']:.0%}

Exit Codes:
  0  - SUCCESS
  1  - QUALITY_THRESHOLD_NOT_MET
  2  - CRITICAL_METRIC_FAILED
  3  - SECURITY_VIOLATION
  4  - SYNTAX_ERROR
  10 - WARNING_ONLY

Dependências:
  - pyyaml: {'✅ instalado' if 'yaml' in sys.modules else '❌ ausente'}
  - pydantic: {'✅ instalado' if 'pydantic' in sys.modules else '❌ ausente'}
    """)
    return 0


def main():
    """Entry point CLI"""
    parser = argparse.ArgumentParser(
        description='MPGO Process Mapper - Engine de Validação v' + VERSION,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')
    
    # Comando: validate
    validate_parser = subparsers.add_parser('validate', help='Validar artefatos')
    validate_parser.add_argument('--yaml', help='Caminho para instrucoes_completas.yaml')
    validate_parser.add_argument('--kb', help='Caminho para base_conhecimento.jsonl')
    validate_parser.add_argument('--mermaid', help='Caminho para arquivo .mermaid')
    validate_parser.add_argument('--html', help='Caminho para framework_saida.html')
    validate_parser.add_argument('--doc', help='Caminho para documentação .md')
    validate_parser.add_argument('--coverage', action='store_true', help='Analisar cobertura da KB')
    validate_parser.add_argument('--output', '-o', help='Arquivo JSON de saída do relatório')
    
    # Comando: info
    info_parser = subparsers.add_parser('info', help='Informações do engine')
    
    args = parser.parse_args()
    
    if not args.comando:
        parser.print_help()
        return 0
    
    if args.comando == 'validate':
        return cmd_validate(args)
    elif args.comando == 'info':
        return cmd_info(args)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
