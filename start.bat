@echo off
REM ============================================================
REM AI Startup Validator - One-Click Startup (thin wrapper)
REM Delegates all startup logic to start.ps1
REM ============================================================

powershell -ExecutionPolicy Bypass -File "%~dp0start.ps1"