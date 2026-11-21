#!/usr/bin/env python3
"""
============================================================
DIGIA - CONTRATOS PÚBLICOS v3.1.0
Engine de Validação e Testes
============================================================
Build: 2026-01-21
Arquitetura: AI GPT Generator v3.1.0
Compliance: ADR-022 (KB-Safe)
============================================================

CLI para validação de artefatos, análise de cobertura,
testes de regressão e scan de segurança SSTI.

Uso:
    python engine.py validate-all
    python engine.py ssti-scan framework_saida.html
    python engine.py coverage-check
    python engine.py golden-test GT-001
    python engine.py build-info
"""

import json
import re
import sys
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

try:
    import yaml
    import click
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
except ImportError as e:
    print(f"❌ Erro: Dependência não instalada: {e}")
    print("Execute: pip install pyyaml click rich --break-system-packages")
    sys.exit(1)

# Console para output formatado
console = Console()

# Diretórios do projeto
BASE_DIR = Path(__file__).parent
ARTIFACTS = {
    'system_prompt': BASE_DIR / 'system_prompt.txt',
    'instrucoes_resumidas': BASE_DIR / 'instrucoes_resumidas.txt',
    'instrucoes_completas': BASE_DIR / 'instrucoes_completas.yaml',
    'base_conhecimento': BASE_DIR / 'base_conhecimento.jsonl',
    'cobertura_esperada': BASE_DIR / 'cobertura_esperada.yaml',
    'framework_saida': BASE_DIR / 'framework_saida.html',
    'icebreaker': BASE_DIR / 'icebreaker.txt'
}


# ============================================================
# VALIDADORES INDIVIDUAIS
# ============================================================

class YAMLValidator:
    """Validador de arquivos YAML"""
    
    @staticmethod
    def validate(filepath: Path) -> Tuple[bool, str]:
        """Valida sintaxe YAML"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
            return True, "YAML válido"
        except yaml.YAMLError as e:
            return False, f"Erro YAML: {e}"
        except Exception as e:
            return False, f"Erro: {e}"


class JSONLValidator:
    """Validador de arquivos JSONL"""
    
    @staticmethod
    def validate(filepath: Path) -> Tuple[bool, str, int]:
        """Valida que cada linha é JSON válido"""
        try:
            total_lines = 0
            errors = []
            
            with open(filepath, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    try:
                        obj = json.loads(line)
                        total_lines += 1
                        
                        # Validar campos obrigatórios
                        required = ['id', 'categoria', 'subcategoria', 'conteudo', 'autoridade']
                        missing = [f for f in required if f not in obj]
                        if missing:
                            errors.append(f"Linha {i}: campos faltando {missing}")
                    
                    except json.JSONDecodeError as e:
                        errors.append(f"Linha {i}: {e}")
            
            if errors:
                return False, "\n".join(errors[:5]), total_lines
            
            return True, f"{total_lines} entradas válidas", total_lines
        
        except Exception as e:
            return False, f"Erro: {e}", 0


class SSTIScanner:
    """Scanner de vulnerabilidades SSTI (Server-Side Template Injection)"""
    
    # Padrões de ataque SSTI (ADR-022)
    PATTERNS = {
        'template_injection': r'(\{\{|\{%)',
        'python_dunder': r'__\w+__',
        'eval_exec': r'(eval|exec)\s*\(',
        'encoding_bypass': r'(base64|hex|rot13|\\x[0-9a-f]{2})',
        'script_tag': r'<script[^>]*>',
        'event_handler': r'on(click|load|error|mouse|key)\s*=',
    }
    
    @staticmethod
    def scan(filepath: Path) -> Tuple[bool, List[Dict]]:
        """Heuristic scan. Safe literal placeholders are not template expressions."""
        violations = []
        try:
            content = filepath.read_text(encoding='utf-8')
            comments = [(m.start(), m.end()) for m in re.finditer(r'<!--.*?-->', content, re.DOTALL)]
            def in_comment(position):
                return any(start <= position < end for start, end in comments)
            for pattern_name, regex in SSTIScanner.PATTERNS.items():
                for match in re.finditer(regex, content, re.IGNORECASE):
                    if in_comment(match.start()):
                        continue
                    if pattern_name == 'template_injection' and match.group() == '{{':
                        placeholder = re.match(r'\{\{([a-z][a-z0-9_]*)\}\}', content[match.start():], re.IGNORECASE)
                        if placeholder:
                            continue
                    violations.append({
                        'pattern': pattern_name,
                        'match': match.group(),
                        'position': match.start(),
                        'context': content[max(0, match.start()-10):match.end()+30].strip()[:80]
                    })
            return len(violations) == 0, violations
        except Exception as e:
            return False, [{'pattern': 'error', 'match': str(e)}]


class CoverageAnalyzer:
    """Analisador de cobertura da knowledge base"""
    
    @staticmethod
    def analyze() -> Tuple[float, Dict]:
        """Analisa cobertura da KB contra cobertura_esperada.yaml"""
        try:
            # Carregar cobertura esperada
            with open(ARTIFACTS['cobertura_esperada'], 'r', encoding='utf-8') as f:
                esperada = yaml.safe_load(f)
            
            # Contar entradas reais na KB
            with open(ARTIFACTS['base_conhecimento'], 'r', encoding='utf-8') as f:
                kb_entries = [json.loads(line) for line in f if line.strip()]
            
            total_kb = len(kb_entries)
            
            # Calcular cobertura por domínio
            dominios = esperada.get('dominios', {})
            cobertura = {}
            
            for dominio_nome, dominio_data in dominios.items():
                min_entradas = dominio_data.get('min_entradas_total', 0)
                
                # Contar entradas do domínio na KB
                entradas_dominio = [
                    e for e in kb_entries 
                    if e.get('categoria') == dominio_nome
                ]
                
                atual = len(entradas_dominio)
                percentual = (atual / min_entradas * 100) if min_entradas > 0 else 100
                
                cobertura[dominio_nome] = {
                    'esperado': min_entradas,
                    'atual': atual,
                    'percentual': percentual,
                    'status': 'PASS' if percentual >= 100 else 'FAIL'
                }
            
            # Score global
            total_esperado = sum(d.get('min_entradas_total', 0) for d in dominios.values())
            score_global = total_kb / total_esperado if total_esperado > 0 else 0
            
            return score_global, cobertura
        
        except Exception as e:
            console.print(f"[red]Erro ao analisar cobertura: {e}[/red]")
            return 0.0, {}


class GoldenTestRunner:
    """Executor de testes Golden (regressão)"""
    
    # Testes Golden definidos
    TESTS = {
        'GT-001': {
            'nome': 'Total de entradas KB >= 50',
            'validador': lambda: JSONLValidator.validate(ARTIFACTS['base_conhecimento'])[2] >= 50
        },
        'GT-002': {
            'nome': 'YAML instrucoes_completas válido',
            'validador': lambda: YAMLValidator.validate(ARTIFACTS['instrucoes_completas'])[0]
        },
        'GT-003': {
            'nome': 'YAML cobertura_esperada válido',
            'validador': lambda: YAMLValidator.validate(ARTIFACTS['cobertura_esperada'])[0]
        },
        'GT-004': {
            'nome': 'HTML framework_saida KB-safe',
            'validador': lambda: SSTIScanner.scan(ARTIFACTS['framework_saida'])[0]
        },
        'GT-005': {
            'nome': 'Cobertura KB >= 0.80',
            'validador': lambda: CoverageAnalyzer.analyze()[0] >= 0.80
        }
    }
    
    @staticmethod
    def run(test_id: Optional[str] = None) -> Dict[str, bool]:
        """Executa testes golden"""
        results = {}
        
        tests_to_run = {test_id: GoldenTestRunner.TESTS[test_id]} if test_id else GoldenTestRunner.TESTS
        
        for tid, test in tests_to_run.items():
            try:
                passed = test['validador']()
                results[tid] = passed
            except Exception as e:
                console.print(f"[red]Erro em {tid}: {e}[/red]")
                results[tid] = False
        
        return results


# ============================================================
# COMANDOS CLI
# ============================================================

@click.group()
@click.version_option(version='3.1.0', prog_name='DIGIA Engine')
def cli():
    """🏛️ DIGIA - Engine de Validação v3.1.0"""
    pass


@cli.command()
def validate_all():
    """Valida todos os artefatos do projeto"""
    console.print("\n[bold cyan]🔍 VALIDAÇÃO COMPLETA DE ARTEFATOS[/bold cyan]\n")
    
    results = {}
    
    # 1. System Prompt
    if ARTIFACTS['system_prompt'].exists():
        size = ARTIFACTS['system_prompt'].stat().st_size
        results['system_prompt'] = {
            'status': 'PASS',
            'message': f'{size:,} bytes'
        }
    else:
        results['system_prompt'] = {'status': 'FAIL', 'message': 'Arquivo não encontrado'}
    
    # 2. Instruções Resumidas
    if ARTIFACTS['instrucoes_resumidas'].exists():
        size = ARTIFACTS['instrucoes_resumidas'].stat().st_size
        if size <= 8000:
            results['instrucoes_resumidas'] = {'status': 'PASS', 'message': f'{size} chars (limite 8,000)'}
        else:
            results['instrucoes_resumidas'] = {'status': 'FAIL', 'message': f'{size} chars EXCEDE 8,000'}
    else:
        results['instrucoes_resumidas'] = {'status': 'FAIL', 'message': 'Arquivo não encontrado'}
    
    # 3. Instruções Completas YAML
    valid, msg = YAMLValidator.validate(ARTIFACTS['instrucoes_completas'])
    results['instrucoes_completas'] = {
        'status': 'PASS' if valid else 'FAIL',
        'message': msg
    }
    
    # 4. Base Conhecimento JSONL
    valid, msg, total = JSONLValidator.validate(ARTIFACTS['base_conhecimento'])
    results['base_conhecimento'] = {
        'status': 'PASS' if valid and total >= 50 else 'FAIL',
        'message': msg
    }
    
    # 5. Cobertura Esperada YAML
    valid, msg = YAMLValidator.validate(ARTIFACTS['cobertura_esperada'])
    results['cobertura_esperada'] = {
        'status': 'PASS' if valid else 'FAIL',
        'message': msg
    }
    
    # 6. Framework Saída HTML
    kb_safe, violations = SSTIScanner.scan(ARTIFACTS['framework_saida'])
    results['framework_saida'] = {
        'status': 'PASS' if kb_safe else 'FAIL',
        'message': 'KB-Safe ✓' if kb_safe else f'{len(violations)} violações SSTI'
    }
    
    # 7. Icebreaker
    if ARTIFACTS['icebreaker'].exists():
        size = ARTIFACTS['icebreaker'].stat().st_size
        if size <= 500:
            results['icebreaker'] = {'status': 'PASS', 'message': f'{size} chars (limite 500)'}
        else:
            results['icebreaker'] = {'status': 'FAIL', 'message': f'{size} chars EXCEDE 500'}
    else:
        results['icebreaker'] = {'status': 'FAIL', 'message': 'Arquivo não encontrado'}
    
    # Exibir resultados
    table = Table(title="Validação de Artefatos", box=box.ROUNDED)
    table.add_column("Artefato", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Detalhes", style="dim")
    
    for artifact, result in results.items():
        status_icon = "✅" if result['status'] == 'PASS' else "❌"
        status_color = "green" if result['status'] == 'PASS' else "red"
        table.add_row(
            artifact,
            f"[{status_color}]{status_icon} {result['status']}[/{status_color}]",
            result['message']
        )
    
    console.print(table)
    
    # Resumo
    total = len(results)
    passed = sum(1 for r in results.values() if r['status'] == 'PASS')
    
    console.print(f"\n[bold]Resultado: {passed}/{total} artefatos válidos[/bold]")
    
    if passed == total:
        console.print("[green]✅ Todos os artefatos validados com sucesso![/green]\n")
        sys.exit(0)
    else:
        console.print("[red]❌ Alguns artefatos falharam na validação[/red]\n")
        sys.exit(1)


@cli.command()
@click.argument('filepath', type=click.Path(exists=True))
def ssti_scan(filepath):
    """Escaneia arquivo HTML em busca de vulnerabilidades SSTI"""
    console.print(f"\n[bold cyan]🔒 SSTI SCANNER - ADR-022[/bold cyan]")
    console.print(f"Arquivo: {filepath}\n")
    
    kb_safe, violations = SSTIScanner.scan(Path(filepath))
    
    if kb_safe:
        console.print(Panel(
            "[green]✅ KB-SAFE: Nenhuma vulnerabilidade SSTI detectada[/green]",
            title="Resultado",
            border_style="green"
        ))
        sys.exit(0)
    else:
        console.print(Panel(
            f"[red]❌ VULNERÁVEL: {len(violations)} violações detectadas[/red]",
            title="Resultado",
            border_style="red"
        ))
        
        table = Table(title="Violações SSTI", box=box.ROUNDED)
        table.add_column("Padrão", style="red")
        table.add_column("Match", style="yellow")
        table.add_column("Contexto", style="dim")
        
        for v in violations[:10]:  # Limitar a 10 primeiros
            table.add_row(
                v.get('pattern', 'unknown'),
                v.get('match', ''),
                v.get('context', '')[:60]
            )
        
        console.print(table)
        
        if len(violations) > 10:
            console.print(f"\n[dim]... e mais {len(violations) - 10} violações[/dim]")
        
        console.print("\n[yellow]⚠️ Corrija as vulnerabilidades antes do deployment[/yellow]\n")
        sys.exit(1)


@cli.command()
def coverage_check():
    """Analisa cobertura da knowledge base"""
    console.print("\n[bold cyan]📊 ANÁLISE DE COBERTURA DA KB[/bold cyan]\n")
    
    score, cobertura = CoverageAnalyzer.analyze()
    
    # Tabela de cobertura por domínio
    table = Table(title="Cobertura por Domínio", box=box.ROUNDED)
    table.add_column("Domínio", style="cyan")
    table.add_column("Esperado", justify="right")
    table.add_column("Atual", justify="right")
    table.add_column("Percentual", justify="right")
    table.add_column("Status", justify="center")
    
    for dominio, data in cobertura.items():
        status_icon = "✅" if data['status'] == 'PASS' else "❌"
        status_color = "green" if data['status'] == 'PASS' else "red"
        
        table.add_row(
            dominio,
            str(data['esperado']),
            str(data['atual']),
            f"{data['percentual']:.1f}%",
            f"[{status_color}]{status_icon} {data['status']}[/{status_color}]"
        )
    
    console.print(table)
    
    # Score global
    console.print(f"\n[bold]Score Global: {score:.2f}[/bold]")
    console.print(f"Threshold Mínimo: 0.80")
    
    if score >= 0.80:
        console.print(f"[green]✅ APROVADO (+{(score - 0.80):.2f} acima do mínimo)[/green]\n")
        sys.exit(0)
    else:
        console.print(f"[red]❌ REPROVADO (-{(0.80 - score):.2f} abaixo do mínimo)[/red]\n")
        sys.exit(1)


@cli.command()
@click.argument('test_id', required=False)
def golden_test(test_id):
    """Executa testes golden de regressão (GT-001 a GT-005)"""
    console.print("\n[bold cyan]🧪 GOLDEN TESTS - REGRESSÃO[/bold cyan]\n")
    
    if test_id and test_id not in GoldenTestRunner.TESTS:
        console.print(f"[red]Teste {test_id} não encontrado[/red]")
        console.print(f"Testes disponíveis: {', '.join(GoldenTestRunner.TESTS.keys())}")
        sys.exit(1)
    
    results = GoldenTestRunner.run(test_id)
    
    # Tabela de resultados
    table = Table(title="Resultados Golden Tests", box=box.ROUNDED)
    table.add_column("ID", style="cyan")
    table.add_column("Teste", style="white")
    table.add_column("Status", justify="center")
    
    for tid in sorted(results.keys()):
        passed = results[tid]
        test_name = GoldenTestRunner.TESTS[tid]['nome']
        status_icon = "✅" if passed else "❌"
        status_color = "green" if passed else "red"
        
        table.add_row(
            tid,
            test_name,
            f"[{status_color}]{status_icon} {'PASS' if passed else 'FAIL'}[/{status_color}]"
        )
    
    console.print(table)
    
    # Resumo
    total = len(results)
    passed = sum(results.values())
    percentage = (passed / total * 100) if total > 0 else 0
    
    console.print(f"\n[bold]Resultado: {passed}/{total} testes passaram ({percentage:.1f}%)[/bold]")
    
    if percentage >= 95:
        console.print("[green]✅ Golden tests APROVADOS (≥95%)[/green]\n")
        sys.exit(0)
    else:
        console.print(f"[red]❌ Golden tests REPROVADOS (<95%)[/red]\n")
        sys.exit(1)


@cli.command()
def build_info():
    """Exibe informações do build e checksums"""
    console.print("\n[bold cyan]ℹ️  BUILD INFORMATION[/bold cyan]\n")
    
    info = {
        'Sistema': 'DIGIA - Contratos Públicos',
        'Versão': '3.1.0',
        'Build Date': '2026-01-21',
        'Arquitetura': 'AI GPT Generator v3.1.0',
        'Compliance': 'Lei 14.133/21, LGPD, ADR-022',
        'Python': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    }
    
    table = Table(title="Sistema", box=box.ROUNDED)
    table.add_column("Propriedade", style="cyan")
    table.add_column("Valor", style="white")
    
    for key, value in info.items():
        table.add_row(key, value)
    
    console.print(table)
    
    # Checksums SHA-256
    console.print("\n[bold]Checksums SHA-256:[/bold]\n")
    
    checksums = Table(box=box.SIMPLE)
    checksums.add_column("Artefato", style="cyan")
    checksums.add_column("SHA-256", style="dim")
    
    for name, filepath in ARTIFACTS.items():
        if filepath.exists():
            with open(filepath, 'rb') as f:
                sha256 = hashlib.sha256(f.read()).hexdigest()
            checksums.add_row(name, sha256[:16] + '...')
        else:
            checksums.add_row(name, '[red]não encontrado[/red]')
    
    console.print(checksums)
    
    # Métricas
    console.print("\n[bold]Métricas:[/bold]\n")
    
    metrics = []
    
    # Total KB entries
    if ARTIFACTS['base_conhecimento'].exists():
        with open(ARTIFACTS['base_conhecimento'], 'r', encoding='utf-8') as f:
            kb_count = sum(1 for line in f if line.strip())
        metrics.append(('Entradas KB', str(kb_count)))
    
    # Coverage score
    score, _ = CoverageAnalyzer.analyze()
    metrics.append(('Score Cobertura', f"{score:.2f}"))
    
    # System prompt size
    if ARTIFACTS['system_prompt'].exists():
        size = ARTIFACTS['system_prompt'].stat().st_size
        metrics.append(('System Prompt', f"{size:,} bytes"))
    
    metrics_table = Table(box=box.SIMPLE)
    metrics_table.add_column("Métrica", style="cyan")
    metrics_table.add_column("Valor", style="white")
    
    for metric, value in metrics:
        metrics_table.add_row(metric, value)
    
    console.print(metrics_table)
    console.print()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️ Operação cancelada pelo usuário[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"\n[red]❌ Erro fatal: {e}[/red]")
        sys.exit(1)
