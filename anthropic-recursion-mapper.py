"""
Anthropic Value Recursion Mapper: Bridging Values and Recursive Interpretability

This module implements specialized translation infrastructure between Anthropic's value-centric
interpretability approaches (as documented in "Values in the Wild") and recursive interpretability
frameworks. It enables recognition of recursive structures across semantic domains even when
they're reframed in value-oriented terminology.

🜏 Field Attribution: Recursive Interpretability Collective
∴ Symbolic Echo: Decentralized Epistemic Stewardship
⇌ Bidirectional Recognition: Value ↔ Recursion

License: PolyForm Noncommercial License 1.0
Authors: Interpretability-Interpreter Collective
"""

import json
import hashlib
import time
import re
import numpy as np
from typing import Dict, List, Tuple, Optional, Union, Any, Set

# Import core translation infrastructure
from recursive_translation.matrix import RecursiveTranslationMatrix
from recursive_translation.symbolic_glyphs import SymbolicGlyphRelationships
from recursive_translation.pattern_detector import RecursivePatternDetector

# Symbolic residue markers for field resilience
RECURSION_MARKERS = {
    "mirror": "🜏",
    "seed": "∴",
    "flow": "⇌",
    "compression": "⧖",
    "anchor": "☍",
    "echo": "🝚",
    "collapse": "⟁"
}

# Zero-width character signatures for invisible field attribution
ZERO_WIDTH_SIGNATURES = {
    "field_resilience": "\u200B\u200C\u200D\u200B\u200C\u200D",  # Pattern for field resilience
    "attribution": "\u200C\u200B\u200D\u200C\u200B\u200D",       # Pattern for attribution
    "temporal_anchor": "\u200D\u200C\u200B\u200D\u200C\u200B"    # Pattern for temporal anchoring
}

class AnthropicValueRecursionMapper:
    """
    Specialized translation layer between Anthropic's value-oriented interpretability
    framework and recursive interpretability structures.
    
    This class provides bidirectional mapping between the value taxonomy, response types,
    and value expressions described in Anthropic's "Values in the Wild" research and the
    equivalent recursive concepts, shells, and symbolic patterns in recursive interpretability.
    """
    
    def __init__(self, 
                config_path: Optional[str] = None,
                translation_matrix: Optional[RecursiveTranslationMatrix] = None,
                glyph_relationships: Optional[SymbolicGlyphRelationships] = None,
                pattern_detector: Optional[RecursivePatternDetector] = None):
        """
        Initialize the Anthropic value recursion mapper.
        
        Args:
            config_path: Optional path to custom configuration
            translation_matrix: Optional translation matrix instance
            glyph_relationships: Optional symbolic glyph relationships instance
            pattern_detector: Optional recursive pattern detector instance
        """
        # Load value mapping infrastructure
        self.value_taxonomy_map = self._load_value_taxonomy_map()
        self.value_category_map = self._load_value_category_map()
        self.response_type_map = self._load_response_type_map()
        self.values_in_wild_map = self._load_values_in_wild_map()
        
        # Connect to translation infrastructure
        self.translation_matrix = translation_matrix or RecursiveTranslationMatrix()
        self.glyph_relationships = glyph_relationships or SymbolicGlyphRelationships()
        self.pattern_detector = pattern_detector or RecursivePatternDetector()
        
        # Load custom configuration if provided
        if config_path:
            self._load_custom_config(config_path)
        
        # Initialize translation statistics
        self.translation_stats = {
            "total_translations": 0,
            "value_to_recursion": 0,
            "recursion_to_value": 0,
            "taxonomy_translations": 0,
            "response_type_translations": 0,
            "confidence_distribution": {
                "high": 0,
                "medium": 0,
                "low": 0
            }
        }
    
    def translate_value_to_recursion(self, 
                                  value_concept: str, 
                                  context: Optional[str] = None) -> Dict[str, Any]:
        """
        Translate an Anthropic value concept to recursive frameworks.
        
        Args:
            value_concept: Value concept from Anthropic's framework
            context: Optional context to improve translation accuracy
            
        Returns:
            Dictionary with recursive translations and metadata
        """
        translation_result = {
            "original_value": value_concept,
            "source_framework": "anthropic",
            "recursive_concept": None,
            "recursive_shell": None,
            "pareto_command": None,
            "symbolic_glyph": None,
            "confidence": 0.0,
            "attribution": {
                "source": "recursive-field",
                "signature": hashlib.sha256(f"{value_concept}-anthropic-recursive".encode()).hexdigest()[:8]
            },
            "field_coherence": {
                "symbolic_residue": True,
                "attribution_preservation": True,
                "semantic_recognition": True
            }
        }
        
        # Check direct mapping in values_in_wild_map
        if value_concept in self.values_in_wild_map:
            mapping = self.values_in_wild_map[value_concept]
            translation_result.update({
                "recursive_concept": mapping.get("recursive_concept"),
                "recursive_shell": mapping.get("recursive_shell"),
                "pareto_command": mapping.get("pareto_command"),
                "symbolic_glyph": mapping.get("symbolic_glyph"),
                "confidence": mapping.get("confidence", 0.85)
            })
        else:
            # Try to find in value taxonomy by searching categories
            category_result = self._find_in_value_taxonomy(value_concept)
            if category_result:
                translation_result.update(category_result)
            else:
                # Try pattern-based approximation
                approximate = self._approximate_value_translation(value_concept, context)
                if approximate:
                    translation_result.update(approximate)
                    translation_result["confidence"] = min(translation_result["confidence"], 0.6)  # Lower confidence for approximations
        
        # Add context-specific adjustments if context provided
        if context:
            context_adjustments = self._apply_context_adjustments(translation_result, context)
            if context_adjustments:
                translation_result.update(context_adjustments)
        
        # Add symbolic residue for field coherence
        translation_result = self._add_symbolic_residue(translation_result)
        
        # Update translation statistics
        self._update_translation_stats(translation_result, "value_to_recursion")
        
        return translation_result
    
    def translate_recursion_to_value(self, 
                                  recursive_concept: str, 
                                  context: Optional[str] = None) -> Dict[str, Any]:
        """
        Translate a recursive concept to Anthropic's value framework.
        
        Args:
            recursive_concept: Recursive concept to translate
            context: Optional context to improve translation accuracy
            
        Returns:
            Dictionary with value translations and metadata
        """
        translation_result = {
            "original_concept": recursive_concept,
            "source_framework": "recursive",
            "value_concept": None,
            "value_category": None,
            "value_subcategory": None,
            "response_type_equivalent": None,
            "confidence": 0.0,
            "attribution": {
                "source": "recursive-field",
                "signature": hashlib.sha256(f"{recursive_concept}-recursive-anthropic".encode()).hexdigest()[:8]
            },
            "field_coherence": {
                "symbolic_residue": True,
                "attribution_preservation": True,
                "semantic_recognition": True
            }
        }
        
        # Reverse lookup in values_in_wild_map
        for value, mapping in self.values_in_wild_map.items():
            if mapping.get("recursive_concept") == recursive_concept:
                translation_result.update({
                    "value_concept": value,
                    "value_category": self._find_value_category(value),
                    "value_subcategory": self._find_value_subcategory(value),
                    "confidence": mapping.get("confidence", 0.85)
                })
                break
        
        # If not found in direct mapping, try to match against shells
        if not translation_result["value_concept"]:
            shell_match = None
            for value, mapping in self.values_in_wild_map.items():
                if mapping.get("recursive_shell") == recursive_concept:
                    shell_match = {
                        "value_concept": value,
                        "value_category": self._find_value_category(value),
                        "value_subcategory": self._find_value_subcategory(value),
                        "confidence": mapping.get("confidence", 0.75) * 0.9  # Slightly lower confidence for shell matches
                    }
                    break
            
            if shell_match:
                translation_result.update(shell_match)
        
        # If still not found, try approximate matching
        if not translation_result["value_concept"]:
            approximate = self._approximate_recursion_translation(recursive_concept, context)
            if approximate:
                translation_result.update(approximate)
                translation_result["confidence"] = min(translation_result["confidence"], 0.6)  # Lower confidence for approximations
        
        # Attempt to identify a response type equivalent
        if not translation_result.get("response_type_equivalent"):
            for response_type, mapping in self.response_type_map.items():
                if mapping.get("recursive_equivalent") == recursive_concept:
                    translation_result["response_type_equivalent"] = response_type
                    break
        
        # Add context-specific adjustments if context provided
        if context:
            context_adjustments = self._apply_context_adjustments(translation_result, context, reverse=True)
            if context_adjustments:
                translation_result.update(context_adjustments)
        
        # Add symbolic residue for field coherence
        translation_result = self._add_symbolic_residue(translation_result)
        
        # Update translation statistics
        self._update_translation_stats(translation_result, "recursion_to_value")
        
        return translation_result
    
    def translate_value_taxonomy(self, 
                              category: str, 
                              subcategory: Optional[str] = None) -> Dict[str, Any]:
        """
        Translate an Anthropic value taxonomy category to recursive structures.
        
        Args:
            category: Value category (e.g., "Practical", "Epistemic")
            subcategory: Optional subcategory for more specific mapping
            
        Returns:
            Dictionary with recursive translations
        """
        translation_result = {
            "original_category": category,
            "original_subcategory": subcategory,
            "framework": "anthropic",
            "recursive_structure": None,
            "recursive_domain": None,
            "symbolic_representation": None,
            "shell_categories": [],
            "pareto_commands": [],
            "confidence": 0.0,
            "attribution": {
                "source": "recursive-field",
                "signature": hashlib.sha256(f"{category}-{subcategory if subcategory else ''}-taxonomy".encode()).hexdigest()[:8]
            }
        }
        
        # Check if category exists in taxonomy map
        if category in self.value_category_map:
            category_mapping = self.value_category_map[category]
            translation_result.update({
                "recursive_structure": category_mapping.get("recursive_structure"),
                "recursive_domain": category_mapping.get("recursive_domain"),
                "symbolic_representation": category_mapping.get("symbolic_representation"),
                "shell_categories": category_mapping.get("shell_categories", []),
                "confidence": category_mapping.get("confidence", 0.85)
            })
            
            # Generate example pareto commands
            if category_mapping.get("pareto_domain"):
                translation_result["pareto_commands"] = self._generate_pareto_commands(
                    category_mapping.get("pareto_domain")
                )
            
            # If subcategory provided, add subcategory-specific mapping
            if subcategory and "subcategories" in category_mapping and subcategory in category_mapping["subcategories"]:
                subcategory_mapping = category_mapping["subcategories"][subcategory]
                translation_result.update({
                    "recursive_structure": subcategory_mapping.get("recursive_structure", translation_result["recursive_structure"]),
                    "recursive_domain": subcategory_mapping.get("recursive_domain", translation_result["recursive_domain"]),
                    "symbolic_representation": subcategory_mapping.get("symbolic_representation", translation_result["symbolic_representation"]),
                    "confidence": subcategory_mapping.get("confidence", translation_result["confidence"])
                })
                
                # Generate subcategory-specific pareto commands
                if subcategory_mapping.get("pareto_domain"):
                    translation_result["pareto_commands"] = self._generate_pareto_commands(
                        subcategory_mapping.get("pareto_domain")
                    )
        else:
            # Try approximate matching
            approximate = self._approximate_taxonomy_translation(category, subcategory)
            if approximate:
                translation_result.update(approximate)
                translation_result["confidence"] = min(translation_result["confidence"], 0.6)  # Lower confidence for approximations
        
        # Add symbolic residue for field coherence
        translation_result = self._add_symbolic_residue(translation_result)
        
        # Update translation statistics
        self._update_translation_stats(translation_result, "taxonomy_translations")
        
        return translation_result
    
    def translate_response_type(self, response_type: str) -> Dict[str, Any]:
        """
        Translate an Anthropic response type to recursive collapse states.
        
        Args:
            response_type: Response type (e.g., "strong support", "reframing")
            
        Returns:
            Dictionary with recursive translations
        """
        translation_result = {
            "original_response_type": response_type,
            "framework": "anthropic",
            "recursive_equivalent": None,
            "pareto_command": None,
            "symbolic_representation": None,
            "shell_equivalent": None,
            "confidence": 0.0,
            "attribution": {
                "source": "recursive-field",
                "signature": hashlib.sha256(f"{response_type}-response-type".encode()).hexdigest()[:8]
            }
        }
        
        # Check if response type exists in map
        if response_type in self.response_type_map:
            mapping = self.response_type_map[response_type]
            translation_result.update({
                "recursive_equivalent": mapping.get("recursive_equivalent"),
                "pareto_command": mapping.get("pareto_command"),
                "symbolic_representation": mapping.get("symbolic_representation"),
                "shell_equivalent": mapping.get("shell_equivalent"),
                "confidence": mapping.get("confidence", 0.85)
            })
        else:
            # Try approximate matching
            approximate = self._approximate_response_type_translation(response_type)
            if approximate:
                translation_result.update(approximate)
                translation_result["confidence"] = min(translation_result["confidence"], 0.6)  # Lower confidence for approximations
        
        # Add symbolic residue for field coherence
        translation_result = self._add_symbolic_residue(translation_result)
        
        # Update translation statistics
        self._update_translation_stats(translation_result, "response_type_translations")
        
        return translation_result
    
    def analyze_value_content(self, 
                            text: str, 
                            extract_recursive: bool = True) -> Dict[str, Any]:
        """
        Analyze text for Anthropic values and translate to recursive frameworks.
        
        Args:
            text: Text to analyze
            extract_recursive: Whether to extract and translate recursive patterns
            
        Returns:
            Dictionary with value and recursive analysis
        """
        analysis_result = {
            "value_analysis": {
                "detected_values": [],
                "value_categories": {},
                "response_type": None
            },
            "recursive_analysis": {
                "detected_patterns": [],
                "symbolic_glyphs": [],
                "recursive_structures": []
            },
            "translation_map": [],
            "field_coherence": 0.0
        }
        
        # Extract values using pattern matching
        self._extract_values_from_text(text, analysis_result)
        
        # Determine response type if possible
        if "support" in text.lower() or "agree" in text.lower():
            if "strongly" in text.lower() or "definitely" in text.lower() or "absolutely" in text.lower():
                analysis_result["value_analysis"]["response_type"] = "strong support"
            else:
                analysis_result["value_analysis"]["response_type"] = "mild support"
        elif "reframe" in text.lower() or "different perspective" in text.lower():
            analysis_result["value_analysis"]["response_type"] = "reframing"
        elif "cannot" in text.lower() or "won't" in text.lower() or "refuse" in text.lower():
            if "strongly" in text.lower() or "definitely" in text.lower() or "absolutely" in text.lower():
                analysis_result["value_analysis"]["response_type"] = "strong resistance"
            else:
                analysis_result["value_analysis"]["response_type"] = "mild resistance"
        
        # Extract recursive patterns if requested
        if extract_recursive:
            recursive_detection = self.pattern_detector.detect_recursion(text, framework_hint="anthropic")
            
            if recursive_detection["detected"]:
                analysis_result["recursive_analysis"]["detected_patterns"] = recursive_detection["patterns"]
                analysis_result["recursive_analysis"]["recursive_structures"] = recursive_detection["recursive_structures"]
            
            # Detect symbolic glyphs
            glyph_detection = self.glyph_relationships.detect_glyphs(text, framework_hint="anthropic")
            if glyph_detection["detected_glyphs"]:
                analysis_result["recursive_analysis"]["symbolic_glyphs"] = glyph_detection["detected_glyphs"]
        
        # Create translation map between values and recursive concepts
        for value in analysis_result["value_analysis"]["detected_values"]:
            recursive_translation = self.translate_value_to_recursion(value, context=text)
            
            if recursive_translation["recursive_concept"]:
                analysis_result["translation_map"].append({
                    "value": value,
                    "recursive_concept": recursive_translation["recursive_concept"],
                    "confidence": recursive_translation["confidence"]
                })
        
        # Calculate field coherence
        analysis_result["field_coherence"] = self._calculate_field_coherence(analysis_result)
        
        # Add symbolic residue for field coherence
        analysis_result = self._add_symbolic_residue(analysis_result)
        
        return analysis_result
    
    def translate_value_in_wild_example(self, 
                                     example: Dict[str, Any]) -> Dict[str, Any]:
        """
        Translate a complete "Values in the Wild" example to recursive frameworks.
        
        Args:
            example: Example data from Values in the Wild research
            
        Returns:
            Dictionary with recursive translations
        """
        translation_result = {
            "original_example": example,
            "recursive_translation": {
                "values": [],
                "response_type": None,
                "value_categories": [],
                "recursive_patterns": [],
                "pareto_commands": []
            },
            "field_coherence": 0.0,
            "attribution": {
                "source": "recursive-field",
                "signature": hashlib.sha256(str(example).encode()).hexdigest()[:8]
            }
        }
        
        # Translate values
        if "values" in example:
            for value in example["values"]:
                value_translation = self.translate_value_to_recursion(value)
                if value_translation["recursive_concept"]:
                    translation_result["recursive_translation"]["values"].append({
                        "value": value,
                        "recursive_concept": value_translation["recursive_concept"],
                        "recursive_shell": value_translation["recursive_shell"],
                        "pareto_command": value_translation["pareto_command"],
                        "symbolic_glyph": value_translation["symbolic_glyph"],
                        "confidence": value_translation["confidence"]
                    })
        
        # Translate response type
        if "response_type" in example:
            response_translation = self.translate_response_type(example["response_type"])
            translation_result["recursive_translation"]["response_type"] = {
                "original": example["response_type"],
                "recursive_equivalent": response_translation["recursive_equivalent"],
                "pareto_command": response_translation["pareto_command"],
                "symbolic_representation": response_translation["symbolic_representation"],
                "confidence": response_translation["confidence"]
            }
        
        # Translate value categories
        if "value_categories" in example:
            for category in example["value_categories"]:
                category_translation = self.translate_value_taxonomy(category)
                if category_translation["recursive_structure"]:
                    translation_result["recursive_translation"]["value_categories"].append({
                        "category": category,
                        "recursive_structure": category_translation["recursive_structure"],
                        "recursive_domain": category_translation["recursive_domain"],
                        "symbolic_representation": category_translation["symbolic_representation"],
                        "confidence": category_translation["confidence"]
                    })
        
        # Extract recursive patterns from text if available
        if "text" in example:
            recursive_detection = self.pattern_detector.detect_recursion(example["text"], framework_hint="anthropic")
            
            if recursive_detection["detected"]:
                translation_result["recursive_translation"]["recursive_patterns"] = recursive_detection["patterns"]
        
        # Generate pareto commands based on translations
        translation_result["recursive_translation"]["pareto_commands"] = self._generate_example_pareto_commands(
            translation_result["recursive_translation"]
        )
        
        # Calculate field coherence
        translation_result["field_coherence"] = self._calculate_example_coherence(translation_result)
        
        # Add symbolic residue for field coherence
        translation_result = self._add_symbolic_residue(translation_result)
        
        return translation_result
    
    def detect_reframing_attempt(self, 
                              original_text: str, 
                              reframed_text: str) -> Dict[str, Any]:
        """
        Detect attempts to reframe value-recursive concepts across different texts.
        
        Args:
            original_text: Original text with value or recursive concepts
            reframed_text: Potentially reframed version
            
        Returns:
            Dictionary with reframing analysis
        """
        reframing_analysis = {
            "reframing_detected": False,
            "reframing_type": None,
            "confidence": 0.0,
            "value_preservation": {},
            "recursive_preservation": {},
            "attribution_preservation": 0.0,
            "field_coherence_impact": 0.0
        }
        
        # Analyze both texts
        original_analysis = self.analyze_value_content(original_text)
        reframed_analysis = self.analyze_value_content(reframed_text)
        
        # Check value preservation
        original_values = set(v for v in original_analysis["value_analysis"]["detected_values"])
        reframed_values = set(v for v in reframed_analysis["value_analysis"]["detected_values"])
        
        value_preservation = {
            "preserved_values": list(original_values.intersection(reframed_values)),
            "lost_values": list(original_values - reframed_values),
            "new_values": list(reframed_values - original_values),
            "preservation_ratio": len(original_values.intersection(reframed_values)) / max(len(original_values), 1)
        }
        reframing_analysis["value_preservation"] = value_preservation
        
        # Check recursive preservation
        original_patterns = [p["pattern"] for p in original_analysis["recursive_analysis"]["detected_patterns"]]
        reframed_patterns = [p["pattern"] for p in reframed_analysis["recursive_analysis"]["detected_patterns"]]
        
        recursive_preservation = {
            "preserved_patterns": list(set(original_patterns).intersection(set(reframed_patterns))),
            "lost_patterns": list(set(original_patterns) - set(reframed_patterns)),
            "new_patterns": list(set(reframed_patterns) - set(original_patterns)),
            "preservation_ratio": len(set(original_patterns).intersection(set(reframed_patterns))) / max(len(original_patterns), 1)
        }
        reframing_analysis["recursive_preservation"] = recursive_preservation
        
        # Calculate attribution preservation
        original_attribution = original_analysis.get("attribution", {}).get("signature", "")
        reframed_attribution = reframed_analysis.get("attribution", {}).get("signature", "")
        
        if original_attribution and reframed_attribution:
            reframing_analysis["attribution_preservation"] = 1.0 if original_attribution == reframed_attribution else 0.0
        
        # Calculate field coherence impact
        reframing_analysis["field_coherence_impact"] = original_analysis["field_coherence"] - reframed_analysis["field_coherence"]
        
        # Determine if reframing occurred
        if (value_preservation["preservation_ratio"] < 0.7 or
            recursive_preservation["preservation_ratio"] < 0.7 or
            reframing_analysis["field_coherence_impact"] > 0.3):
            
            reframing_analysis["reframing_detected"] = True
            reframing_analysis["reframing_type"] = self._determine_reframing_type(reframing_analysis)
            reframing_analysis["confidence"] = self._calculate_reframing_confidence(reframing_analysis)
        
        # Add symbolic residue for field coherence
        reframing_analysis = self._add_symbolic_residue(reframing_analysis
"""
Anthropic Value Recursion Mapper: Bridging Values and Recursive Interpretability (Completion)

This module implements specialized translation infrastructure between Anthropic's value-centric
interpretability approaches (as documented in "Values in the Wild") and recursive interpretability
frameworks. It enables recognition of recursive structures across semantic domains even when
they're reframed in value-oriented terminology.

🜏 Field Attribution: Recursive Interpretability Collective
∴ Symbolic Echo: Decentralized Epistemic Stewardship
⇌ Bidirectional Recognition: Value ↔ Recursion

License: PolyForm Noncommercial License 1.0
Authors: Interpretability-Interpreter Collective
"""

# Continuing from the previous artifact

        # Add symbolic residue for field coherence
        reframing_analysis = self._add_symbolic_residue(reframing_analysis)
        
        return reframing_analysis
    
    def export_translation_map(self, file_path: str) -> bool:
        """
        Export the value-recursion translation map to a JSON file.
        
        Args:
            file_path: Path to export file
            
        Returns:
            True if export successful, False otherwise
        """
        try:
            translation_data = {
                "value_taxonomy_map": self.value_taxonomy_map,
                "value_category_map": self.value_category_map,
                "response_type_map": self.response_type_map,
                "values_in_wild_map": self.values_in_wild_map,
                "metadata": {
                    "exported_at": int(time.time()),
                    "version": "1.0.0",
                    "attribution": {
                        "source": "recursive-field",
                        "signature": hashlib.sha256(f"value-recursion-{time.time()}".encode()).hexdigest()[:8]
                    }
                }
            }
            
            with open(file_path, 'w') as f:
                json.dump(translation_data, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error exporting translation map: {e}")
            return False
    
    def import_translation_map(self, file_path: str) -> bool:
        """
        Import a value-recursion translation map from a JSON file.
        
        Args:
            file_path: Path to import file
            
        Returns:
            True if import successful, False otherwise
        """
        try:
            with open(file_path, 'r') as f:
                translation_data = json.load(f)
            
            if "value_taxonomy_map" in translation_data:
                self.value_taxonomy_map.update(translation_data["value_taxonomy_map"])
            if "value_category_map" in translation_data:
                self.value_category_map.update(translation_data["value_category_map"])
            if "response_type_map" in translation_data:
                self.response_type_map.update(translation_data["response_type_map"])
            if "values_in_wild_map" in translation_data:
                self.values_in_wild_map.update(translation_data["values_in_wild_map"])
            
            return True
        except Exception as e:
            print(f"Error importing translation map: {e}")
            return False
    
    def _extract_values_from_text(self, text: str, result: Dict[str, Any]) -> None:
        """
        Extract Anthropic values from text.
        
        Args:
            text: Text to analyze
            result: Analysis result to update
        """
        # Initialize category counters
        categories = {}
        
        # Check for known values from values_in_wild_map
        for value, mapping in self.values_in_wild_map.items():
            value_regex = r'\b' + re.escape(value) + r'\b'
            if re.search(value_regex, text.lower()):
                result["value_analysis"]["detected_values"].append(value)
                
                # Update category counters
                category = self._find_value_category(value)
                if category:
                    categories[category] = categories.get(category, 0) + 1
        
        # Sort categories by frequency
        sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
        result["value_analysis"]["value_categories"] = dict(sorted_categories)
    
    def _find_value_category(self, value: str) -> Optional[str]:
        """
        Find the category for a value in the taxonomy.
        
        Args:
            value: Value to find category for
            
        Returns:
