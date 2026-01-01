<script lang="ts">
</script>

<section id="contact" class="contact">
	<div class="section-header">
		<h2><span class="hash">#</span> Start a Project</h2>
	</div>
	<div class="contact-content">
		<div class="code-block">
			<pre><span class="keyword">const</span> project = {'{'}<br/>  client: <span class="string">"you"</span>,<br/>  approach: <span class="string">"0-to-1"</span>,<br/>  quality: <span class="string">"production-ready"</span>,<br/>  contact: <span class="string">"<a href="mailto:contact@codepasture.com">contact@codepasture.com</a>"</span><br/>{'}'};</pre>
		</div>
		<p>Have something to build? Let's talk.</p>
		<a href="mailto:contact@codepasture.com" class="btn-primary">Send Email</a>
	</div>
</section>

<style>
	.contact {
		padding: 5rem 2rem;
		max-width: var(--max-width);
		margin: 0 auto;
		border-top: 1px solid var(--color-border);
	}

	.section-header {
		margin-bottom: 2rem;
	}

	.section-header h2 {
		font-size: 1.5rem;
		font-weight: 600;
		margin-bottom: 0.5rem;
	}

	.hash {
		color: var(--color-text-muted);
		margin-right: 0.25rem;
	}

	.contact-content {
		max-width: 500px;
	}

	.code-block {
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		padding: 1.5rem;
		margin-bottom: 1.5rem;
		overflow-x: auto;
	}

	.code-block pre {
		font-family: var(--font-mono);
		font-size: 0.9rem;
		line-height: 1.6;
		margin: 0;
	}

	.keyword {
		color: var(--color-purple);
	}

	.string {
		color: var(--color-accent);
	}

	.code-block a {
		color: var(--color-accent);
		text-decoration: none;
	}

	.code-block a:hover {
		text-decoration: underline;
	}

	.contact-content p {
		color: var(--color-text-muted);
		margin-bottom: 1.5rem;
	}

	.btn-primary {
		display: inline-block;
		background: var(--color-accent);
		color: var(--color-bg);
		padding: 0.875rem 1.5rem;
		border-radius: var(--radius-md);
		text-decoration: none;
		font-weight: 600;
		font-size: 0.9rem;
		transition: background var(--transition-fast);
	}

	.btn-primary:hover {
		background: var(--color-accent-hover);
	}

	@media (max-width: 768px) {
		.contact {
			padding: 3rem 1.5rem;
		}
	}
</style>
