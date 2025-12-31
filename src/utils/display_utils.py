"""
Display utilities for the Todo Python Console App.

Implements formatting functions for displaying tasks with due dates and recurrence indicators.
"""

from datetime import date
from typing import Optional
from todo import Task
from utils.date_utils import is_overdue, days_overdue


def format_task_display(task: Task) -> str:
    """
    Formats a task for display in the console with appropriate indicators.
    
    Args:
        task: The task to format
        
    Returns:
        Formatted string representation of the task
    """
    status = "[x]" if task.completed else "[ ]"
    
    # Add overdue indicator if applicable
    due_indicator = ""
    if task.due_date:
        if is_overdue(task.due_date):
            due_indicator = "[OVERDUE] "
        elif days_overdue(task.due_date) == 0:  # Due today
            due_indicator = "[Due Today] "
        else:  # Due in the future
            days = days_overdue(task.due_date)
            if days < 0:  # Negative means days until due
                due_indicator = f"[Due in {abs(days)} days] "
            else:
                due_indicator = f"[{abs(days)} days overdue] "
    
    # Add recurrence indicator if applicable
    recur_indicator = ""
    if task.recurrence_frequency:
        recur_indicator = "[RECUR] "
    
    # Format the task string
    formatted_task = f"{due_indicator}{status} {task.id}: {task.title}"
    if task.description:
        formatted_task += f" - {task.description}"
    
    formatted_task += f" {recur_indicator}"
    
    return formatted_task


def get_task_due_status(task: Task) -> str:
    """
    Returns a string describing the due date status of a task.
    
    Args:
        task: The task to check
        
    Returns:
        String describing the due date status
    """
    if not task.due_date:
        return ""
    
    if is_overdue(task.due_date):
        days = days_overdue(task.due_date)
        return f"(due {days} days ago)"
    elif days_overdue(task.due_date) == 0:  # Due today
        return "(Due today)"
    else:  # Due in the future
        days = abs(days_overdue(task.due_date))
        return f"(due in {days} days)"


def get_recurrence_indicator(task: Task) -> str:
    """
    Returns a string indicating the recurrence status of a task.
    
    Args:
        task: The task to check
        
    Returns:
        String indicating recurrence status
    """
    if task.recurrence_frequency:
        return f"[{task.recurrence_frequency.upper()}]"
    return ""


def format_task_line(task: Task) -> str:
    """
    Formats a task for display in a list with all indicators.
    
    Args:
        task: The task to format
        
    Returns:
        Formatted string for list display
    """
    status = "[x]" if task.completed else "[ ]"
    
    # Determine due date indicator
    due_status = get_task_due_status(task)
    due_indicator = f" {due_status}" if due_status else ""
    
    # Determine recurrence indicator
    recur_indicator = f" {get_recurrence_indicator(task)}" if task.recurrence_frequency else ""
    
    # Format tags
    tags_str = ""
    if task.tags:
        tags_str = f" [{','.join(task.tags)}]"
    
    # Priority indicator
    priority_indicator = ""
    if task.priority == "High":
        priority_indicator = " [H]"
    elif task.priority == "Medium":
        priority_indicator = " [M]"
    elif task.priority == "Low":
        priority_indicator = " [L]"
    
    # Combine all parts
    formatted_line = f"{status} {task.id}: {task.title}{due_indicator}{recur_indicator}{priority_indicator}{tags_str}"
    
    if task.description:
        formatted_line += f" - {task.description}"
    
    return formatted_line